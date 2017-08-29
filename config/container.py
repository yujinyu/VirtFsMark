# -*- coding: UTF-8 -*-
import os

docker_svc_path = "/lib/systemd/system/docker.service"


#
# 测试之前删除其他运行的容器，并拉去测试需要的镜像
#
def pre_work_for_docker(clt, img):
    try:
        ids_list = clt.containers.list()
        if len(ids_list) > 0:
            yn = input("Some containers are running! "
                       "Stop them and continue to test ?[Y,N]")
            if yn == "N" or yn == "N":
                for cid in ids_list:
                    cid.stop()
                    cid.remove()
            else:
                exit(0)
        clt.images.pull(img)
    except:
        print("Prepare work Failed!")
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
def del_stopped_container(clt):
    ids_list = clt.containers.list(True)
    if len(ids_list) > 0:
        for cid in ids_list:
            cid.remove()


#
# 创建并运行一定数目的执行指定命令的容器
#
def create_and_run(clt, image, cmd, vol, num):
    for i in range(0, num):
        clt.containers.create(image=image, command=cmd, volumes=vol, working_dir='/')
    ids_list = clt.containers.list(True)
    for cid in ids_list:
        cid.start()
