#!/usr/bin/python2.5
import sys
from prdg.util.file import file_to_str, str_to_file
from .util import replace_command


def flatten_latex_str(text):
    return replace_command(
        'input',
        lambda fname: flatten_latex_str(file_to_str(fname)),
        text
    )


def flatten_latex_file(in_path, out_path):
    text = file_to_str(in_path)
    new_text = flatten_latex_str(text)
    str_to_file(new_text, out_path, do_not_overwrite=False)


def main():
    flatten_latex_file(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
