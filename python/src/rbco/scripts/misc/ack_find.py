"""Roughly equivalent to: find -iname "*$QUERY*"

Usage:
  ack-find [options] <query>

Options:
  -h --help         Print this message.
"""
from docopt import docopt
from clom import clom
import sys


def main():
    arguments = docopt(__doc__)
    query = arguments['<query>']
    cmd = clom.find('-iname', '*{0}*'.format(query))
    print >> sys.stderr, cmd
    cmd.shell.execute()

if __name__ == '__main__':
    main()
