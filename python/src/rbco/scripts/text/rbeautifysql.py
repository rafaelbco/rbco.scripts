#!/usr/bin/python
"""
USAGE: rbeautifysql.py
Pretty-print to STDOUT the SQL code read from STDIN.
"""
import sys
import re

TOP_LEVEL_KEYWORDS = ['select', 'from', 'where', 'group by', 'having', 'into']
TOP_LEVEL_KEYWORDS_PATTERN = '(' + '|'.join(TOP_LEVEL_KEYWORDS) + ')'


def main():
    input = sys.stdin.read().strip()
    parts = [p.strip() for p in re.compile(TOP_LEVEL_KEYWORDS_PATTERN, re.I).split(input) if p]
    parts = [((p.lower() in TOP_LEVEL_KEYWORDS) and p) or ('    ' + p) for p in parts]

    print '\n'.join(parts)

if __name__ == '__main__':
    main()
