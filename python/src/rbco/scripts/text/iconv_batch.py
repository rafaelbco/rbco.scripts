#coding=utf8
"""Convert files from one encoding to another.

Usage:
  iconv_batch [options] <from> <to> <file>...

Convert <from> one encoding <to> another. Only files detected to be in the the
given <from> encoding will be converted.

Encoding names must conform to the output of "file --mime-type" and be
understood by Python as a valid encoding name.

Some encoding names following these rules: utf-8, iso-8859-1 and us-ascii

Options:
  -h, --help        Show this message.
  -d, --dry-run     Do not write to any file, only prints what would be
                    converted or not.
"""
from docopt import docopt
from clom import clom


def detect_encoding(path):
    return clom.file(path, **{'mime-encoding': True}).shell.first().split(':')[1].strip().lower()


def main():
    arguments = docopt(__doc__)
    from_encoding = arguments['<from>']
    to_encoding = arguments['<to>']
    files = arguments['<file>']
    dry_run = arguments['--dry-run']

    for path in files:
        print 'Processing {0} ...'.format(path)
        if detect_encoding(path) != from_encoding:
            print 'Not encoded in {0}. Skipped.'.format(from_encoding)
            print
            continue

        with open(path, 'r') as f:
            u_text = f.read().decode(from_encoding)

        s_text = u_text.encode(to_encoding)

        if dry_run:
            print 'Would be converted {0}.'.format(to_encoding)
        else:
            with open(path, 'w') as f:
                f.write(s_text)
            print 'Converted to {0}.'.format(to_encoding)

        print

if __name__ == '__main__':
    main()
