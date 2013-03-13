#!/bin/bash
# USAGE: cp_rand_dirs.sh DEST
# Copy random dirs inside the current dir to DEST.
# Warning: direct subdirs are not copied because mindepth == 2.

find -mindepth 2 -type d -print0 | sort -R -z | xargs -0 cp -R -t $1
