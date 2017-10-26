from src.funcModules import cntrs

image = "virtfsmark:network"

def ab_svr(client, path2df, overlay_network, svr_name):
    # cntrs.build_images(client, path2df, image)
    svr = client.containers.run(image=image, command="/bin/bash",
                                network=overlay_network, name=svr_name, detach=True)
    svr.exec_run(cmd="httpd -k start")


def ab_clt(client, path2df, overlay_network, svr_name, vol , outfile):
    # cntrs.build_images(client, path2df, image)
    cmd = "ab -n 10000 -c 100 http://%s:80 >> %s"%(svr_name, outfile)
    clt = client.containers.run(image=image, command="/bin/bash",
                          network=overlay_network, volumes=vol, detach=True)

    clt.exec_run(cmd)