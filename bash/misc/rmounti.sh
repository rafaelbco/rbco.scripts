#!/bin/bash

ISO_DIR=~/iso
ISO_FILE=__cd.iso
MOUNT_DIR=/media/cdrom
DEVICE=/dev/hdb

mount -t iso9660 -o loop $ISO_DIR/$ISO_FILE $MOUNT_DIR
