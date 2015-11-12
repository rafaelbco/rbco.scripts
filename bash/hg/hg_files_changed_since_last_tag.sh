#!/bin/bash
LASTTAG=$(hg tags --quiet | grep -vw tip | head -n1)
hg status -n --rev $LASTTAG:tip
