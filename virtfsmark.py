# -*- coding: UTF-8 -*-
import docker
from config.container import *
from config.cpus import *
from run_config import *


image = "yujinyu/ubuntu-sysbench:ex"


if __name__ == "__main__":

    client = docker.from_env()
    pre_work_for_docker(client, image)
    cpu_num = get_num_cpus()
    # todo
    for dev in storage_devices:
        create_and_run(client, image, " ", " ", 1)
    for bk_fs in backing_fs:
        create_and_run(client, image, " ", " ", 1)
    for sd in storage_devices:
        create_and_run(client, image, " ", " ", 1)

    for n in range(cpu_num - 1, 0, -1):
        # 根据启用的CPU个数创建相应个数的测试容器
        set_cpus_onoff(n, "0")
        create_and_run(client, image, " ", " ", n)
