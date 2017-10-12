#!/usr/bin/env bash
# $1 type
# $2 The longest duration of the test running
# $3 min file size
# $3 path to output file
sysbench --test=fileio --file-num=1 --file-block-size=4096 --file-test-mode=$1 --time=$2  --file-total-size=$3 prepare
sysbench --test=fileio --file-num=1 --file-block-size=4096 --file-test-mode=$1 --time=$2  --file-total-size=$3 run > $4
sysbench --test=fileio --file-num=1 --file-block-size=4096 --file-test-mode=$1 --time=$2  --file-total-size=$3 cleanup