#coding=utf8
"""Usage: ftpserver [<port>]

Serve the current directory via FTP. Anonymous user has full read and write permissions.

<port> defaults to 2121
"""
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import sys


PERMS_ALL = 'elradfmwM'
DEFAULT_PORT = 2121


def main():
    port = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PORT

    authorizer = DummyAuthorizer()
    authorizer.add_user('test', 'test', '.', perm=PERMS_ALL)
    authorizer.add_anonymous(os.getcwd(), perm=PERMS_ALL)

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:{port}
    address = ('', port)
    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()
