import docker


def pre_work(img):
    try:
        client = docker.from_env ()
        ids_list = client.containers.list()
        if len(ids_list) > 0:
            yn = input("Some containers are running! "
                       "Stop them and continue to test ?[Y,N]")
            if yn == "N" or yn == "N":
                for cid in ids_list:
                    cid.stop()
                    cid.remove()
            else:
                exit(0)
        client.images.pull(img)
    except:
        print("Prepare work Failed!")
        exit(-1)


def mkfs(fs, dev);
