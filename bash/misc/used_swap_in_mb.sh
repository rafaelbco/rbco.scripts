#!/bin/sh
free -m | grep "^Swap" | tr -s '[:space:]' | cut -d' ' -f 3
