#!/usr/bin/python
"""
Print out all citations made using \cite and \citeonline.

USAGE: showcites.py FILES
"""

import sys
import re

CITES_PATTERN = r'\cite(?:online)?{(\S+?)}'

def main():
    files = sys.argv[1:]
    cites = set()

    for f in files:
        text = open(f).read()
        cites_f = re.findall(CITES_PATTERN, text)
        for c in cites_f:
            cites |= set(c.split(','))

    print '\n'.join(cites)

if __name__ == '__main__':
    main()

