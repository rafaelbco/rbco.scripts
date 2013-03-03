#!/bin/bash

PERIOD=0.5

if [ -z "$1" ]; then
        echo
        echo usage: $0 network-interface
        echo
        echo e.g. $0 eth0
        echo
        exit
fi

R1=`cat /sys/class/net/$1/statistics/rx_bytes`
T1=`cat /sys/class/net/$1/statistics/tx_bytes`

sleep $PERIOD

R2=`cat /sys/class/net/$1/statistics/rx_bytes`
T2=`cat /sys/class/net/$1/statistics/tx_bytes`

TBPS=`echo "($T2 - $T1) / $PERIOD" | bc`
RBPS=`echo "($R2 - $R1) / $PERIOD" | bc`

TKBPS=`echo "($TBPS / 1024)" | bc`
RKBPS=`echo "($RBPS / 1024)" | bc`

printf "In: %.3d Out: %.3d (kB/s)\n" $RKBPS $TKBPS

