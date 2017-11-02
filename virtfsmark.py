# -*- coding: UTF-8 -*-

import docker
import os
import time

from src import network, file
from src.funcModules import cntrs, auxFuncs

vol = {"/mnt": "/mnt"}

out_dir = "/home/result/"
tmp_dir = "/mnt/result/"

benchmarks = {"mutilfiles", "file", "network"}

local_host = "192.168.3.69"
clt_host = "192.168.3.69"

if __name__ == "__main__":
    path2df = os.path.join(os.getcwd(), "src/image_built")
    clt = docker.from_env()
    cntrs.del_containers(clt, True)
    for type in benchmarks:
        os.system(
            "cp -fr %s %s" % (
                os.path.join(os.getcwd(), "src/docfiles/%s" % type),
                os.path.join(os.getcwd(), "src/image_built/Dockerfile")))
        # if type == "network":
        #     network.build_image(clt_host, path2df)
        #     network.build_image("192.168.3.75", path2df)
        #     network.build_image("192.168.3.79", path2df)

        #    network.ab_svr(clt, path2df, "olnet1", "ab_svr1")
        #    network.test("192.168.3.75", "ab_svr1", "root", "135668", vol, tmp_dir, out_dir)
        #    network.test("192.168.3.79", "ab_svr1", "root", "135668", vol, tmp_dir, out_dir)
        if type == "file":
            # os.system("mkdir -p /mnt/test && cd /mnt/test "
            #           "&& touch file")
            os.system("mkdir -p %s" % out_dir)
            os.system("mkdir -p %s" % tmp_dir)

            file.build_image(clt_host, path2df)
            file.fio_test(clt_host, vol, tmp_dir)
            os.system("mv %s %s" % (tmp_dir, out_dir + "Lfileres" +
                                    time.strftime('%y%m%d%H%M', time.localtime(time.time()))))
            #
            # if type == "mutilfiles":
            #     # cntrs.build_image(clt, path2df, "virtfsmarks:mf")
            #     cmd = "python /multifiles.py 128 10000"
            #     cntrs.create_and_run_simple(clt,"virtfsmarks:mf", cmd, vol)
