#!/bin/sh
free -m | grep "^-/\+" | tr -s '[:space:]' | cut -d' ' -f 3
