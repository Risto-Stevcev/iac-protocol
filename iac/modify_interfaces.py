#!/usr/bin/env python
import argparse
import sys
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
_INTERFACES = 'interfaces.py'

title = 'Inter-Application Communication protocol'
__author__ = 'Risto Stevcev'
__version__ = '0.205'


def modify(application_name, enable=True):
    new_interfaces = []
    with open(os.path.join(_ROOT, _INTERFACES), 'r') as f:
        for line in f:
            if application_name in line and enable:
                new_interfaces.append(line.replace('#', ''))
            elif application_name in line and not enable:
                new_interfaces.append("#" + line)
            else:
                new_interfaces.append(line)
    with open(os.path.join(_ROOT, _INTERFACES), 'w') as f:
        for line in new_interfaces:
            f.write(line)

def read():
    with open(os.path.join(_ROOT, _INTERFACES), 'r') as f:
        print(f.read())

def enable(application_name):
    modify(application_name, enable=True)

def disable(application_name):
    modify(application_name, enable=False)


argparser = argparse.ArgumentParser(
        description='Modify interfaces for %s v%s - by %s.' % (title, __version__, __author__))
argparser.add_argument('-a', '--application', type=str, dest='app',  
        help='application name')
argparser.add_argument('-s', '--show', action='store_const', const=True, dest='show_apps',
        help='show apps')

group = argparser.add_mutually_exclusive_group()
group.add_argument('--enable', action='store_const', const=True, dest='enable_app', 
        help='enable application (default)')
group.add_argument('--disable', action='store_const', const=False, dest='enable_app', 
        help='disable application')
argparser.set_defaults(enable_app=True, show_apps=False)
args = argparser.parse_args()


def main():
    if args.app and args.enable_app:
        enable(args.app)
    elif args.app and not args.enable_app:
        disable(args.app)

    if args.show_apps:
        with open(os.path.join(_ROOT, _INTERFACES), 'r') as f:
            print(f.read())

if __name__ == '__main__':
    main()
