# -*- coding: UTF-8 -*-
import time

import docker

from configs.container import *
from configs.cpus import *

out_dir = "/mnt/result/"
image = "virtfsmark:fc26"
vol = {"/mnt": "/mnt"}


def oltp_test(res_dir, type, duration, server_host):
    port = {'3306': '3306'}
    cmd_server = "./root/mark_loads/mysql_server.sh"
    client.containers.create(image, cmd_server, ports=port, hostname="mysql_server", name="mysql_server").start()
    cmd_pre = "./root/mark_loads/%s %s %s %s" % ("mysql_pre.sh", type, duration, server_host)
    client.containers.create(image, cmd_pre).start()
    cmd = "./root/mark_loads/%s %s %s %s %s" % ("mysql_run.sh", type, duration, server_host, res_dir)
    for n in range(4, 17, 16):
        # while len(client.containers.list()) > 0:
        #     time.sleep(10)
        # for cid in client.containers.list(True):
        #     cid.remove()

        create_and_run(client, image, cmd + "%02d" % n + "-log-", port, vol, n)

    while len(client.containers.list()) > 1:
        time.sleep(10)
    del_containers(client, True)


if __name__ == "__main__":
    dockerfile = os.path.join(os.getcwd(), "image_built/")
    print("The path to Dockerfile is: %s." % dockerfile)

    client = docker.from_env()
    prepare_work(client)
    # build_images(client, dockerfile, image)
    os.system("mkdir -p %s" % out_dir)

    # os.system("mv %s %s" % (out_dir, "%s/res%s" % (os.getcwd(),time.strftime('%y%m%d%H%M',time.localtime(time.time())))))
