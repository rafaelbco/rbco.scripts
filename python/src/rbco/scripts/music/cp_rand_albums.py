#coding=utf8
"""Copy random album directories to a destination directory.

Usage:
  cp_rand_albums [options] <source> <dest>

Select random album directories inside <source> and copy them to <dest>.
The <source> directory is searched recursively.

A directory is considered an album directory if it contains at least one
file with the "mp3" extension. Album directories are copied non-recursively,
i.e subdirectories are not copied.

Directory structure is not preserved.

Options:
  -h --help          Show this message.
"""

from docopt import docopt
import walkdir
from pathlib import Path
import random
import os
import shutil


def copy_dir_non_recursively(source, dest):
    """
    Copy the `source` directory into the `dest` directory. Files contained in `source` are copied
    but subdirectories are not.

    Arguments are `Path` instances.
    """
    full_dest_str = str(dest[source.name])
    os.mkdir(full_dest_str)
    for f in source:
        if f.is_file():
            shutil.copy(str(f), full_dest_str)


def main():
    arguments = docopt(__doc__)
    source = arguments['<source>']
    dest = arguments['<dest>']

    dirs = walkdir.dir_paths(walkdir.filtered_walk(source))
    dirs = [d for d in dirs if d != '.' if list(Path(d).glob('*.mp3'))]
    random.shuffle(dirs)

    for d in dirs:
        print 'Copying {0} ...'.format(d)
        copy_dir_non_recursively(Path(d), Path(dest))

if __name__ == '__main__':
    main()
