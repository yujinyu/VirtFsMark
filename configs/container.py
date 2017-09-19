# -*- coding: UTF-8 -*-
import os
from random import Random

docker_svc_path = "/lib/systemd/system/docker.service"


def random_str(randomlength=6):
    string = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for l in range(randomlength):
        string += chars[random.randint(0, length)]
    return string


#
# 测试之前删除其他运行的容器，并拉去测试需要的镜像
#
def pre_work_for_docker(clt, work_dir, image):
    try:
        if clt.images.list(image) is not None:
            clt.images.remove(image, force=True)
        clt.images.build(path=work_dir, tag=image)
        print("Build image Successfully!")

        ids_list = clt.containers.list()
        if len(ids_list) > 0:
            yn = input("Stop containers and continue to test ?[Y/N]")
            if yn != "y" and yn != "Y":
                exit(0)
        del_containers(clt, True)
    except Exception as e:
        print(str(e))
        exit(-1)


#
# 停止docker daemon运行
#
def docker_svc_stop():
    """
    :return:
    """
    if 0 == os.system("systemctl stop docker.service"):
        print("Docker daemon stopped")
        os.system("umount -lf $(df | awk '{print $6}'| grep /var/lib/docker )")
        os.system("umount -lf $(cat /proc/mounts | grep docker | awk '{print $2}')")
        os.system("umount -lf /var/lib/docker")
        os.system("rm -rf /var/lib/docker/*")
        return 0
    else:
        print("Failed to stop docker daemon")
        return -1


#
# 重启docker daemon
#
def docker_svc_restart():
    """
    :return:
    """
    os.system("systemctl daemon-reload")
    if 0 == os.system("systemctl restart docker.service"):
        print("Restart Docker daemon successfully")
        return 0
    else:
        print("Failed to restart docker daemon")
        return -1


#
# 将docker容器的存储驱动配置为new_driver
#
def config_storage_driver(new_driver):
    fpr = open(docker_svc_path, 'r+')
    lines_in_file = fpr.readlines()
    fpr.close()
    i = 0
    for line in lines_in_file:
        if "ExecStart" in line:
            if "fd://" in line:  # deb pkg arch
                lines_in_file[i] = "ExecStart=/usr/bin/dockerd --insecure-registry 192.168.3.51:5000 -s " + \
                                   new_driver + " -H fd://" + line[-1]
            else:  # rpm pkg arch
                lines_in_file[i] = "ExecStart=/usr/bin/dockerd --insecure-registry 192.168.3.51:5000 -s " + \
                                   new_driver + line[-1]
            break
        else:
            i += 1
    fpw = open(docker_svc_path, 'w+')
    fpw.writelines(lines_in_file)
    fpw.close()


#
# 删除已经停止运行的容器
#
def del_containers(clt, force=False):
    ids_list = clt.containers.list(force)
    if len(ids_list) > 0:
        for cid in ids_list:
            if cid.status == "running":
                cid.stop()
            cid.remove(force=force)


#
# 创建并运行一定数目的执行指定命令的容器
#
def create_and_run(clt, image, cmd, vol, num):
    for i in range(0, num):
        clt.containers.create(image=image, command=cmd + random_str(4), volumes=vol, working_dir='/')
    ids_list = clt.containers.list(True)
    for cid in ids_list:
        cid.start()

