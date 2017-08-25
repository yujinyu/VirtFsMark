# -*- coding: UTF-8 -*-
import sys, os


#
# 将dev设备格式化为fs类型文件系统
#
def dev_mkfs(fs, dev):
    """
        param fs: target filesystem, e.g. ext4
        param dev: format device, e.g. /dev/sdb
        return: sucess 0, fail 1
    """
    if fs not in []:
        print >> sys.stderr, ("Unrecognized file system %s" % fs)
        exit(-1)
    if fs in ["ext4", "btrfs", "xfs"]:
        os.system("mkfs." + fs + "-f " + dev)
    elif fs in ["zfs"]:
        os.system("zpool create -f zfspool " + dev)
        os.system("zfs create -o mountpoint=/var/lib/docker zfspool/docker")


#
# 如果之前文件系统类型为zfs，则需要使用之后对其进行销毁
#
def destory_fs(dev):
    pre_fs = os.popen("df -T|grep " + dev + " |awk \'{print $2}\'").readlines()[0]
    if pre_fs in ["zfs"]:
        os.system("zfs destroy -r zfspool")
        os.system("zpool destroy zfspool")

