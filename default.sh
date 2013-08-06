#!/bin/bash

addr=`netstat -rn |  awk '/default/ {print $2}'`

echo "the defualt gateway of this network is: " $addr
sleep 1
ping $addr
