#!/bin/bash

DEVICE=$1
ISO=$2

rm -f $ISO
readom dev=$DEVICE -f=$ISO
