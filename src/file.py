import os

import docker

from src.funcModules.cntrs import build_images, create_and_run

image = "virtfsmark:file"
dir2df = os.path.join(os.getcwd(), "image_built/")
print("The path to Dockerfile is: %s." % dir2df)


def filePrepare():
    clt = docker.from_env()
    build_images(clt, dir2df, image)

def fileTest(shareLevel, type, duration, server_host, res_dir):
    if shareLevel == "H" or shareLevel == "h":

        create_and_run()
    exit(0)