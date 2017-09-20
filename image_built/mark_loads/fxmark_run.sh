#!/usr/bin/env bash
# $1 bench type
# $2 The longest duration of the test running
# $3 directio flag
# $4 path to output file

fxmark --type $1 --ncore 1 --nbg 0 --duration $2 --directio $3 --root /root/mark_loads > $4