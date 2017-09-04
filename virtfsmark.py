# -*- coding: UTF-8 -*-
import os, docker
from configs.container import *
from configs.cpus import *

image = "virtfsmark:latest"

if __name__ == "__main__":
    dockerfile = os.path.join(os.getcwd(),"images/")
    print(dockerfile)

    client = docker.from_env()
    pre_work_for_docker(client, dockerfile, image)



    # todo
