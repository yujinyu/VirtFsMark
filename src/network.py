import docker
import time
from src.funcModules import cntrs
from src.funcModules import auxFuncs

image = "virtfsmark:network"


def ab_svr(client, overlay_network, svr_name):
    svr = client.containers.create(image=image, network=overlay_network, name=svr_name, stdin_open=True, detach=True)
    svr.start()
    svr.exec_run(cmd="httpd -k start")


def ab_clt(client, overlay_network, svr_name, vol, outfile):
    cmd = "ab -n 1000000 -c 100 http://%s:80/ >> %s && exit" % (svr_name, outfile)
    cmd = "ab -n 1000000 -c 100 http://%s:80/" % svr_name
    print(cmd)
    client.containers.run(image=image, command=cmd, network=overlay_network, volumes=vol, stdin_open=True,
                          detach=True).logs()
    # clt = client.containers.create(image=image, network=overlay_network, volumes=vol,stdin_open=True,detach=True)
    # clt.start()
    # clt.exec_cmd(cmd)


def build_image(clt_host, path2df):
    clt_clt = docker.DockerClient(base_url="tcp://%s:2376" % clt_host)
    cntrs.build_images(clt_clt, path2df, image)


def test(clt_host, ab_svr, username, passwd, vol, tmp_dir, out_dir):
    clt_clt = docker.DockerClient(base_url="tcp://%s:2376" % clt_host)
    cntrs.del_containers(clt_clt, True)
    ssh_clt = auxFuncs.Rhost(clt_host, username, passwd)
    ssh_clt.connect()
    ssh_clt.exec_cmd("mkdir -p %s && mkdir -p %s" % (tmp_dir, out_dir))
    ssh_clt.close()

    outfile = tmp_dir + auxFuncs.random_str(6)
    ab_clt(clt_clt, "olnet1", ab_svr, vol, outfile)
    ssh_clt.connect()
    ssh_clt.exec_cmd("mv %s %s" % (tmp_dir, out_dir + "networkres" +
                                   time.strftime('%y%m%d%H%M', time.localtime(time.time()))))
    ssh_clt.close()
