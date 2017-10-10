# -*- coding: UTF-8 -*-
import os
from random import Random

def random_str(randomlength=6):
    string = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for l in range(randomlength):
        string += chars[random.randint(0, length)]
    return string



def get_mem_size():
    fd = os.popen("cat /proc/meminfo|grep \"MemTotal:\"")
    out = fd.read()
    fd.close()
    return int(int(out.split(" ")[-2]) / (1024.0 * 1024.0) + 0.5)


storage_devices = ["SSD", "HDD"]
backing_filesystems = ["ext4", "btrfs", "xfs", "ext4_no_jnl", "tmpfs", "zfs"]
storage_drivers = ["aufs", "overlay2", "btrfs", "xfs", "zfs"]
mem_size = get_mem_size()
