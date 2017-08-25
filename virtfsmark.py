# -*- coding: UTF-8 -*-
import docker

from config.container import *
from config.cpus import *

pkg_list = ["xfsprogs", "btrfs-tools", "f2fs-tools", "jfsutils", "reiserfsprogs", "nilfs-tools", "zfsutils-linux"]
image = "192.168.3.51:5000/admin/ubuntu-sysbench:ex-fs"


def is_installed(pkg_name):
    state, stout = subprocess.getstatusoutput("dpkg --get-selections | grep " + pkg_name + " | awk \'{print $2}\'")
    if state == 0 and stout == "install":
        return True
    else:
        return False


def pkg_install(pkg_name):
    state, stout = subprocess.getstatusoutput("sudo apt-get install -y " + pkg_name)
    if state == 0:
        return True
    else:
        return False


def catch_ctrl_c(signum, frame):
    print ("cat Ctrl+C, Go to exit...")
    exit (0)


if __name__ == "__main__":
    #
    # 配置运行环境，安装必要的软件包
    #
    ls = " "
    for pkg in pkg_list:
        if not is_installed(pkg):
            ls.join(" " + pkg)
    if ls is " ":
        exit(1)
    elif not pkg_install(ls):
        exit(-1)

    client = docker.from_env()
    pre_work_for_docker(client, image)
    cpu_num = get_num_cpus()
    # todo
    for n in range(cpu_num-1, 0, -1):
        # 根据启用的CPU个数创建相应个数的测试容器
        set_cpus_onoff(n, "0")
        create_and_run(client, image, " ", " ", n)

