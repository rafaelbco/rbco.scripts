#!/usr/bin/python2.5
import os.path
import sys
from .util import get_master_name, pdflatex, bibtex, clean
from .latex_flatten import flatten_latex_file


def parse_args(args=sys.argv[1:]):
    """Return: (options_list, target)"""
    return (args[0:-1], args[-1])


def main():
    (options, target_tex) = parse_args()

    if os.path.dirname(target_tex):
        raise RuntimeError(
            'This program must be executed in the same dir as the target.'
        )

    options_str = ' '.join(options)
    if '-dir ' not in options_str:
        raise RuntimeError(
            '-dir option is required, otherwise an ugly '
            'directory name will be used.'
        )

    master_name = get_master_name(target_tex)

    master_name_flat = master_name + '_flat'
    flat_tex = master_name_flat + '.tex'

    try:
        # Generate a flat .tex.
        flatten_latex_file(target_tex, flat_tex)

        # Compile the bibliography.
        pdflatex(flat_tex)
        bibtex(master_name_flat)

        cmd = 'latex2html ' + ' '.join(options) + ' ' + flat_tex
        print cmd
        os.system(cmd)
    finally:
        # Cleanup.
        clean(master_name_flat, ('pdf', 'pdf.mk', 'tex'))

if __name__ == '__main__':
    main()
