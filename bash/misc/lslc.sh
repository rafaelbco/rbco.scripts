#!/bin/bash
# USAGE: $0
# List files in the directory and its line counts.
ls -1p | grep -v "/$" | xargs wc -l
