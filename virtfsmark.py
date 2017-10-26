# -*- coding: UTF-8 -*-

import docker
import os
import time

from src import network
from src.funcModules import cntrs, auxFuncs

vol = {"/mnt": "/mnt"}
out_dir = "/home/result/"
tmp_dir = "/mnt/result/"

clt_host = "192.168.3.75"

if __name__ == "__main__":
    svr_clt = docker.from_env()
    cntrs.del_containers(svr_clt, True)
    os.system(
        "cp -fr %s %s" % (
            os.path.join(os.getcwd(), "src/docfiles/network"), os.path.join(os.getcwd(), "src/image_built/Dockerfile")))
    path2df = os.path.join(os.getcwd(), "src/image_built")
    network.ab_svr(svr_clt, path2df, "olnet1", "ab_svr1")

    clt_clt = docker.DockerClient(base_url="tcp://%s:2376" % clt_host)
    cntrs.del_containers(clt_clt, True)
    clt75 = auxFuncs.Rhost(clt_host, "root", "135668")
    clt75.connect()
    clt75.exec_cmd("mkdir -p %s && mkdir -p %s" % (tmp_dir, out_dir))
    clt75.close()

    outfile = tmp_dir + auxFuncs.random_str(6)

    network.ab_clt(clt_clt, path2df, "olnet1", "ab_svr1", vol, outfile)

    clt75.connect()
    clt75.exec_cmd("mv %s %s" % (tmp_dir, out_dir + "res" +
                                 time.strftime('%y%m%d%H%M', time.localtime(time.time()))))
    clt75.close()
