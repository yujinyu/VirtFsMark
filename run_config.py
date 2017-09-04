# -*- coding: UTF-8 -*-
storage_devices = ["SSD", "HDD"]
backing_filesystems = ["ext4", "btrfs", "xfs", "ext4_no_jnl", "tmpfs", "zfs"]
storage_drivers = ["aufs", "overlay2", "btrfs", "xfs", "zfs"]

microbench_types = [
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
