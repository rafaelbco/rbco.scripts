#!/bin/bash
# USAGE: cp_filelist.sh FILELIST DEST
# Given a path to a file (FILELIST) containing file paths (one per line), copy these files to DEST.
FILELIST="$1"
OUTDIR="$2"
cat $FILELIST | xargs -d "\n" cp -t $OUTDIR
