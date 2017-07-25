# -*- coding: UTF-8 -*-
path_proc = "/proc/cpuinfo"
path_sys = "/sys/devices/system/cpu/"

docker_svc_path = "/lib/systemd/system/docker.service"
image = "192.168.3.51:5000/admin/virtfsmark:latest"

pkg_list = ["xfsprogs", "btrfs-tools", "f2fs-tools", "jfsutils", "reiserfsprogs", "nilfs-tools", "zfsutils-linux"]

storage_devices = ["SSD", "HDD"]
backing_fs = ["ext4", "btrfs", "xfs", "ext4_no_jnl", "tmpfs", "zfs"]
bench_types = [
    # write/write
    "DWAL",
    "DWOL",
    "DWOM",
    "DWSL",
    "MWRL",
    "MWRM",
    "MWCL",
    "MWCM",
    "MWUM",
    "MWUL",
    "DWTL",

    # filebench
    "filebench_varmail",
    "filebench_oltp",
    "filebench_fileserver",

    # dbench
    "dbench_client",

    # read/read
    "MRPL",
    "MRPM",
    "MRPH",
    "MRDM",
    "MRDL",
    "DRBH",
    "DRBM",
    "DRBL"
]

