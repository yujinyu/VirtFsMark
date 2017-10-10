# -*- coding: UTF-8 -*-

import docker

from src.cntrs import *

out_dir = "/mnt/result/"
image = "virtfsmark:fc26"
vol = {"/mnt": "/mnt"}


if __name__ == "__main__":
    dockerfile = os.path.join(os.getcwd(), "image_built/")
    print("The path to Dockerfile is: %s." % dockerfile)

    client = docker.from_env()
    prepare_work(client)
    # build_images(client, dockerfile, image)
    os.system("mkdir -p %s" % out_dir)

    # os.system("mv %s %s" % (out_dir, "%s/res%s" % (os.getcwd(),time.strftime('%y%m%d%H%M',time.localtime(time.time())))))
