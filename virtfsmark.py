# -*- coding: UTF-8 -*-

import docker
import os
import time

from src import file
from src.funcModules import cntrs

vol = {"/mnt": "/mnt"}
out_dir = "/home/Result/res%s" % time.strftime('%y%m%d%H%M', time.localtime(time.time()))
tmp_dir = "/mnt/result/"
image = "virtfsmark:sysb"


if __name__ == "__main__":
    client = docker.from_env()
    cntrs.del_containers(client, True)
    path2df = os.path.join(os.getcwd(), "src/image_built")
    cntrs.prepare_work(client)
    os.system("mkdir -p %s" % tmp_dir)
    file.fio_test(client, image, path2df, vol, tmp_dir)
    os.system("mv %s %s" % (tmp_dir, out_dir))
