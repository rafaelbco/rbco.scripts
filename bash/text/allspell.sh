#!/bin/bash
# Usage: allspell.sh EXTENSION
# Spell check all files with the given extension, recursing into subdirectories.

find -name "*.$1" -exec aspell -l pt_br -c {} \;


