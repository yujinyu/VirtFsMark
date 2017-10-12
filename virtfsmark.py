# -*- coding: UTF-8 -*-

import docker

from src.cntrs import *

out_dir = "/mnt/result/"
image = "virtfsmark:fc26"
vol = {"/mnt": "/mnt"}


if __name__ == "__main__":

    client = docker.from_env()
    prepare_work(client)
    os.system("mkdir -p %s" % out_dir)