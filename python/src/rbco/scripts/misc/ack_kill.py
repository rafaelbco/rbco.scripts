"""Kill process found by ack_ps.

Usage:
  ack-kill [options] <query> [--] [<kill_option>...]

Process found by calling "ack-ps <query>" will be killed.
Everything after the optional "--" is passed to "kill" as options.

Options:
  -h --help         Print this message.
"""
from docopt import docopt
from clom import clom
from clom.shell import CommandError
from rbco.scripts.misc.ack_ps import ack_ps

ACK_PS_OPTS = {
    'pid-only': True,
}


def print_and_exec(cmd):
    print str(cmd)
    cmd.shell.execute()


def get_pids(query):
    return list(ack_ps(query, pid_only=True))


def main():
    arguments = docopt(__doc__)
    query = arguments['<query>']
    kill_options = arguments['<kill_option>']

    pids = get_pids(query)
    if not pids:
        print 'No process found.'
        return

    print 'PIDs found: {0}'.format(' '.join(pids))

    kill_args = list(kill_options) + pids

    print_and_exec(clom.kill(*kill_args))

    pids = get_pids(query)
    if not pids:
        print 'Killed !'
        return

    print 'Remaining processes:'

    try:
        clom.ps(pid=','.join(pids), format='pid,user,cmd').shell.execute()
    except CommandError as e:
        # Return code 1 for ps means no process was found.
        if e.return_code == 1:
            pass

if __name__ == '__main__':
    main()
