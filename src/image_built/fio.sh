#!/usr/bin/env bash
# $1: -rw,    read, write, randwrite, randread, rw(readwrite), randrw
# $2: -bs,    blocksize
# $3: -buffered=1 or -direct=1
# $4: -ioengine,  sync, psync, libaio
# $5: the file redirect the output to
fio -filename=/test/file -rw=$1 -bs=$2 $3 -ioengine=$4 -thread -size=8G -runtime=120 -name=mytest > $5