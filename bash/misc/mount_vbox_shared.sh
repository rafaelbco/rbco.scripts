#!/bin/bash
SCRIPT="$(basename $0)"
USAGE="${SCRIPT} <share>"
SHARE="$1"

if [[ -z ${SHARE} ]]; then
    echo ${USAGE}
    exit 1
fi

GID=$(getent group ${USER} | cut -d: -f3)
OPTS="rw,uid=${UID},gid=${GID}"
TARGET="${HOME}/shared/${SHARE}"

mkdir -p "${TARGET}"

if mountpoint --quiet "${TARGET}"; then
    echo "Already mounted."
else
    sudo mount --types=vboxsf --options="${OPTS}" "${SHARE}" "${TARGET}"
fi

echo "${TARGET}"
