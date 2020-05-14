#!/bin/bash
INPUT="$@"
if [[ -z ${INPUT} ]]; then
    INPUT="${PWD}"
fi

echo ${INPUT}
echo ${INPUT} | tr -d '\n' |  xclip
