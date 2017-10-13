import os


def get_mem_size():
    fd = os.popen("cat /proc/meminfo|grep \"MemTotal:\"")
    out = fd.read()
    fd.close()
    return int(int(out.split(" ")[-2]) / (1024.0 * 1024.0) + 0.5)