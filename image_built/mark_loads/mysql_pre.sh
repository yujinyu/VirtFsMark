#!/usr/bin/env bash
# $1 oltp type
# $2 The longest duration of the test running
# $3 mysql server ip or hostname

sysbench /usr/share/sysbench/$1.lua --db-driver=mysql --mysql-db=mysql --mysql-user=root --mysql-password=123456 --time=$2 --threads=1 --mysql-host=$3 --mysql-port=3306 prepare