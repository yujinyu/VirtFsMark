# -*- coding: UTF-8 -*-
import signal, docker
from env_config import *
from cpus_config import *
from container_config import *
from variables_defined import pkg_list, image

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

