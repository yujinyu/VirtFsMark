#!/usr/bin/env bash
# $1 oltp type
# $2 The longest duration of the test running
# $3 path to output file
sysbench prepare
sysbench run
sysbench cleanup