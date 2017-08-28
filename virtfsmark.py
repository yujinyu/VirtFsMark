# -*- coding: UTF-8 -*-
import docker
import subprocess

from config.container import *
from config.cpus import *

image = "192.168.3.51:5000/admin/ubuntu-sysbench:ex-fs"


def pkg_install(pkg_name, version): # version : deb ? rpm
    if version == "deb":
        state, stout = subprocess.getstatusoutput("sudo apt-get install -y " + pkg_name)
        if state == 0:
            return True
        else:
            return False
    if version == "rpm":
        state, stout = subprocess.getstatusoutput("sudo yum install -y " + pkg_name)
        if state == 0:
            return True
        else:
            return False



def catch_ctrl_c(signum, frame):
    print ("cat Ctrl+C, Go to exit...")
    exit (0)


if __name__ == "__main__":

    client = docker.from_env()
    pre_work_for_docker(client, image)
    cpu_num = get_num_cpus()
    # todo
    for n in range(cpu_num-1, 0, -1):
        # 根据启用的CPU个数创建相应个数的测试容器
        set_cpus_onoff(n, "0")
        create_and_run(client, image, " ", " ", n)

