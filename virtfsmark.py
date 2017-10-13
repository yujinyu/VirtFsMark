# -*- coding: UTF-8 -*-

import docker

from src.funcModules.cntrs import *

out_dir = "/mnt/result/"
image = "virtfsmark:fc26"
vol = {"/mnt": "/mnt"}


if __name__ == "__main__":

    client = docker.from_env()
    path2df = os.path.join(os.getcwd(),"src/image_built")
    prepare_work(client)
    build_images(client,path2df,image)

    os.system("mkdir -p %s" % out_dir)