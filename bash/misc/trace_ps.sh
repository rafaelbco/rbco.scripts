#!/bin/bash

PROC=$1

while [ 1 ]; 
do
    sleep 0.1s
    ps ax | grep -i $PROC   
done
