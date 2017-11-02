#!/usr/bin/env bash
fio -filename=/mnt/test/file -direct=1 -thread -rw=$1 -ioengine=psync -bs=512k -size=2G -runtime=60 -name=mytest > $2