#!/bin/bash
ack_ps "" | percol | tr -s ' ' | cut -d' '  -f2 | xargs kill $2 $3 $4 $5 $6 $7
