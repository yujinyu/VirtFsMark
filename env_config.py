# -*- coding: UTF-8 -*-
import os

storage_devices = ["SSD", "HDD"]
backing_filesystems = ["ext4", "btrfs", "xfs", "ext4_no_jnl", "tmpfs", "zfs"]
storage_drivers = ["aufs", "overlay2", "btrfs", "xfs", "zfs"]


def get_mem_size():
    fd = os.popen("cat /proc/meminfo|grep \"MemTotal:\"")
    out = fd.read()
    fd.close()
    return int(int(out.split(" ")[-2]) / (1024.0 * 1024.0) + 0.5)


mem_size = get_mem_size()
