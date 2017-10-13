import time

import docker

from src.funcModules.cntrs import create_and_run, del_containers

image = "virtfsmark:oltp"
volume = {"/mnt": "/mnt"}
port = {'3306': '3306'}


def oltp_test(res_dir, type, duration, server_host):
    client = docker.from_env()
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

        create_and_run(client, image, cmd + "%02d" % n + "-log-", port, volume, n)

    while len(client.containers.list()) > 1:
        time.sleep(10)
    del_containers(client, True)
