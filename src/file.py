import time
import docker

from src.funcModules import cntrs, lock_stat

image = "virtfsmark:file"


def build_image(clt_host, path2df):
    clt_clt = docker.DockerClient(base_url="tcp://%s:2376" % clt_host)
    cntrs.build_image(clt_clt, path2df, image)


def fio_test(clt_host, vol, outdir):
    clt = docker.DockerClient(base_url="tcp://%s:2376" % clt_host)
    cntrs.del_containers(clt, True)
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        # for bs in ["4k","8k","16k","32k","64k","128k","256k","512k","1024k","2048k"]:
        bs = "4k"
        lock_stat.start()
        for j in range(1, i + 1):
            cmd = "./fio.sh %s %s %s %s %s" % (
                "write", bs, "-buffered=1", "libaio", outdir + "fiores%s-%s" % (str(i), str(j)))
            print(cmd)
            clt.containers.create(image=image, command=cmd, volumes=vol, working_dir='/')
        ids_list = clt.containers.list(True)
        for cid in ids_list:
            cid.start()

        ids_list = clt.containers.list()
        while len(ids_list) > 0:
            time.sleep(15)
            ids_list = clt.containers.list()
        lock_stat.stop()
        lock_stat.get(outdir + "lockstat%s-%s" % (str(i), bs), head=True)
        cntrs.del_containers(clt, True)
