#!/bin/bash
# USO: portscan.sh HOST
nc -z -v "$1" 1-65535  2>&1 | grep succeeded
