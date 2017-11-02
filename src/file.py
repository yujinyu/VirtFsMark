import os
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
    for i in [1,3,7,15]:
        lock_stat.start()
        for j in range(1,i+1):
            cmd = "./fio.sh write %s" % outdir + "fiores%s-%s"%(str(i),str(j))
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
        lock_stat.get(outdir + "lockstat%s"%str(i), False, True)
        cntrs.del_containers(clt, True)