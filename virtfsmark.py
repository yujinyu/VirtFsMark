# -*- coding: UTF-8 -*-
import os, docker,time
from configs.container import *
from configs.cpus import *

out_dir = "/mnt/result/"
image = "virtfsmark:f26"

if __name__ == "__main__":
    dockerfile = os.path.join(os.getcwd(),"image_built/")
    print("The path to Dockerfile is: %s." % dockerfile)

    client = docker.from_env()
    pre_work_for_docker(client, dockerfile, image)
    os.system("mkdir -p %s", out_dir)

    bench = "DRBM"
    vol = {"/mnt":"/mnt"}
    cmd = "./root/mark_loads/run.sh %s 1 %s"%(bench, out_dir)

    for n in range(1,17):
        while len(client.containers.list())>0:
            time.sleep(10)
        for cid in client.containers.list(True):
            cid.remove()
        create_and_run(client,image,cmd+"%02d"%n+"-log-",vol,n)

    while len(client.containers.list())>0:
        time.sleep(10)

    os.system("mv %s %s"%(out_dir,"/root/res01"))
