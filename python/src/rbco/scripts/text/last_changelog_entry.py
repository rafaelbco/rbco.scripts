#coding=utf8
"""Get the last (topmost) entry on the changelog.

Changelog is searched on HISTORY.txt and docs/HISTORY.txt. It can also be
sepecified as an option.

Usage:
  last_changelog_entry [options]

Options:
  -h, --help                Imprime esta mensagem.
  -f FILE, --file=FILE      Specify FILE as the changelog.
"""
from docopt import docopt
import os
import re

CHANGELOG_PATHS = ('HISTORY.txt', os.path.join('docs', 'HISTORY.txt'))


def find_file(paths):
    for p in paths:
        if os.path.exists(p):
            return p


def main():
    arguments = docopt(__doc__)

    changelog_path = arguments['--file'] or find_file(CHANGELOG_PATHS)
    change = []

    with open(changelog_path, 'r') as f:
        for l in f:
            if not change:
                if l.startswith('- ') or l.startswith('* '):
                    change.append(l[2:].strip())
            else:
                if l.startswith(' '):
                    change.append(l.strip())
                else:
                    break

    s = '\n'.join(change)

    print re.sub(r'\s+', ' ', s)

if __name__ == '__main__':
    main()
