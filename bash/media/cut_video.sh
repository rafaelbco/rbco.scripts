#!/bin/bash
# USAGE: cut_video.sh <infile> <start> <duration> <outfile>
# start and duration are in format hh:mm:ss
avconv -i "$1" -ss "$2" -t "$3" -codec copy "$4"
