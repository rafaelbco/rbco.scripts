#!/usr/bin/python
"""
USAGE: oneline.py
Read input from STDING and convert it to one line, by replacing all occurrences of repeated space
chars (space, newline and tab) to a single space. Output is written to STDOUT.
"""
import sys
import re


def main():
    s = sys.stdin.read()
    print re.sub(r'\s+', ' ', s)

if __name__ == '__main__':
    main()
