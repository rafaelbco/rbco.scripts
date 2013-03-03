#!/usr/bin/python
"""
Usage: buildout_versions.py

Execute this script in the buildout directory and it will output the versions pinned by the buildout
configuration.
"""
import re
import os
from commands import getoutput

BIN_BUILDOUT = os.path.join('bin', 'buildout')


def main():
    s = getoutput(BIN_BUILDOUT + ' annotate')

    pattern = re.compile(r'^\n+', re.MULTILINE)
    secoes = re.split(pattern, s)

    pacotes = []

    for sec in secoes:
        if sec.startswith('[versions]'):
            lines = sec.split('\n')
            for l in lines:
                if '=' in l:
                    (package, version) = l.split('=')
                    pacotes.append((package.strip(), version.strip()))

            break

    pacotes = sorted(pacotes, key=lambda x: x[0])
    print '[versions]'
    for (p, v) in pacotes:
        print '%s = %s' % (p, v)

if __name__ == '__main__':
    main()
