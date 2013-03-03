#!/bin/bash
# USAGE: ordered_cp.sh DEST
# Copy everything in the current directory to DEST in alphabetically order.
find -print0 | sort -z | xargs -0 cp -v --parents -t $1
