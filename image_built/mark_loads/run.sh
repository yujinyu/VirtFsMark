#!/usr/bin/env bash

fxmark --type $1 --ncore 1 --nbg 0 --duration 60 --directio $2 --root /root/mark_loads > $3