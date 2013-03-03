#!/bin/bash
# Uso: png2eps ARQUIVO.PNG ARQUIVO.EPS
pngtopnm "$1" > "$1".tmp.pnm
pnmtops -noturn "$1".tmp.pnm > "$1".tmp.ps
ps2eps -O "$1".tmp.ps
mv "$1".tmp.ps $2
rm -f "$1".tmp.{eps,p{nm,s}}
