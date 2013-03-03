#!/usr/bin/python
import re
import os

RE_VERSION = r"""version\s*=\s*(?:'|")(\S+)(?:'|")"""

def sub_in_file(pattern, filename, replacement):
    with open(filename, 'r') as f:
        s = f.read()

    new = re.sub(pattern, replacement, s)

    if s != new:
        with open(filename, 'w') as f:
            f.write(new)

def main():
    with open('setup.py', 'r') as f:
        s = f.read()
        version = re.findall(RE_VERSION, s)[0]
        tag = 'v' + version.replace('.', '_')
        cmd = 'cvs tag -R "%s"' % tag
        print cmd
        os.system(cmd)

if __name__ == '__main__':
    main()