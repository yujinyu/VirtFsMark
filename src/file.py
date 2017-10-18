import os
import time

import docker

from src.funcModules import cntrs, lock_stat

image = "virtfsmark:file"
dir2df = os.path.join(os.getcwd(), "image_built/")
print("The path to Dockerfile is: %s." % dir2df)


def filePrepare():
    clt = docker.from_env()
    cntrs.build_images(clt, dir2df, image)

def fileTest(shareLevel, type, duration, server_host, res_dir):
    if shareLevel == "H" or shareLevel == "h":
        cntrs.create_and_run()
    exit(0)



def fio_test(clt, image, path2df, vol, outdir):
    cntrs.build_images(clt, path2df, image)
    os.system("mkdir -p /mnt/test && cd /mnt/test && touch file")
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