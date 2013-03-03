#!/bin/bash
# USO: split2gb.sh ORIGEM DIR_DESTINO
split -d -b 2000M $1 $2/`basename $1`.
