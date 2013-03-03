#!/usr/bin/python2

import os

if __name__ == '__main__':
    base_path = os.path.abspath(os.path.join(os.getcwd(), 'bash'))

    directories = [os.path.join(base_path, d) for d in os.listdir(base_path)]
    directories = [d for d in directories if os.path.isdir(d)]

    print 'export PATH=' + ':\\\n'.join(['$PATH'] + directories)
