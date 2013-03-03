#!/usr/bin/python
import re
import os
from datetime import datetime

RE_CHANGELOG_UNRELEASED_ENTRY = re.compile(r"""^([\d\.]+)\s+\(unreleased\)\s*$""", re.I | re.M)
RE_VERSION = re.compile(r"""version\s*=\s*(?:'|")(\S+)-dev(?:'|")""", re.I)

def sub_in_file(pattern, filename, replacement):
    with open(filename, 'r') as f:
        s = f.read()

    new = re.sub(pattern, replacement, s)

    if s != new:
        with open(filename, 'w') as f:
            f.write(new)


def main():
    data = datetime.now().strftime('%d-%m-%Y')
    sub_in_file(RE_CHANGELOG_UNRELEASED_ENTRY, 'docs/HISTORY.txt',  r'\1 (%s)' % data)
    sub_in_file(RE_VERSION, 'setup.py',  r"version = '\1'")

    os.system('cvs diff setup.py')
    os.system('cvs diff docs/HISTORY.txt')

if __name__ == '__main__':
    main()
