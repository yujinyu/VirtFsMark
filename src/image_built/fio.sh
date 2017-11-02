#!/usr/bin/env bash
fio -filename=/test/file -direct=1 -thread -rw=$1 -ioengine=psync -bs=1024k -size=4G -runtime=60 -name=mytest > $2