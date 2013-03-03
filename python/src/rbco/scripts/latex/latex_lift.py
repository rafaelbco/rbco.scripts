#!/usr/bin/python2.5
"""
lifter.py: Shift Latex sectioning commands, e.g: \section -> \chapter,
\subsection -> \section, etc.

USAGE: lifter.py N FILES

    N: number of levels to shift. Can be negative.
    FILES: paths to .tex files


Files are modified in place.
"""

USAGE = __doc__

import re
import sys

SECTION_TYPES = [
    'subsubsection',
    'subsection',
    'section',
    'chapter',
    'part'
]

SECTION_CMD_REGEX = r'\\(%s){' % '|'.join(SECTION_TYPES)

LEN_SECTION_TYPES = len(SECTION_TYPES)

def lift(latex, n):
    if n == 0:
        return latex

    def repl(match):
        section_type = match.group(1)
        section_type_idx = SECTION_TYPES.index(section_type)
        new_section_type_idx = section_type_idx + n

        if ((new_section_type_idx < 0)
            or (new_section_type_idx >= LEN_SECTION_TYPES)):

            raise RuntimeError("Can't lift %s by %d" % (section_type, n))

        new_section_type = SECTION_TYPES[new_section_type_idx]

        return r'\%s{' % new_section_type

    return re.sub(SECTION_CMD_REGEX, repl, latex)

def lift_file(filename, n):
    f = open(filename, 'r')
    latex = f.read()
    f.close()

    new_latex = lift(latex, n)
    f = open(filename, 'w')
    f.write(new_latex)
    f.close()

def main():
    if len(sys.argv) < 3:
        print USAGE
        sys.exit(1)

    n = int(sys.argv[1])
    filenames = sys.argv[2:]

    for filename in filenames:
        lift_file(filename, n)

if __name__ == '__main__':
    main()

