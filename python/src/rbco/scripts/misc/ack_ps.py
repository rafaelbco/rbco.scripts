"""Roughly equivalent to: ps aux | grep -i $QUERY

Usage:
  ack-ps [options] <query>

Options:
  -h --help         Print this message.
  -p --pid-only     Print only the PIDs.
"""
from docopt import docopt
from clom import clom
from clom.shell import CommandError
import os

GREP_FILTER_OPTS = {
    'ignore-case': True
}

GREP_EXCLUDE_SELF_OPTS = {
    'invert-match': True,
    'word-regexp': True,
}

PS_ARGS = ('aux',)
PS_OPTS = {
    'no-headers': True
}

PS_PID_ONLY_ARGS = ('ax',)
PS_PID_ONLY_OPTS = {
    'no-headers': True,
    'format': ','.join(('pid', 'user', 'cmd',))
}


def ack_ps(query, pid_only=False):
    (ps_args, ps_opts) = (PS_ARGS, PS_OPTS) if not pid_only else (PS_PID_ONLY_ARGS, PS_PID_ONLY_OPTS)

    ps = clom.ps(*ps_args, **ps_opts)
    grep_filter = clom.grep(query, **GREP_FILTER_OPTS)
    grep_exclude_self = clom.grep('\({0}\|grep\)'.format(os.getpid()), **GREP_EXCLUDE_SELF_OPTS)

    cmd = ps.pipe_to(grep_filter.pipe_to(grep_exclude_self))

    lines = tuple()
    try:
        lines = cmd.shell.iter()
    except CommandError as e:
        # Return code 1 for grep means nothing was found.
        if e.return_code == 1:
            pass

    if pid_only:
        lines = (l.strip().split()[0] for l in lines)

    return lines


def main():
    arguments = docopt(__doc__)
    lines = ack_ps(query=arguments['<query>'], pid_only=arguments['--pid-only'])
    for l in lines:
        print l



if __name__ == '__main__':
    main()
