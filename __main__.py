#!/usr/bin/python3.7
# -*- encoding: utf-8 -*-

import argparse

from views import console_input
from views.MainViewModel import MainViewModel

parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument(
    '-pwd',
    '--password',
    help='Set password.',
    type=str
)
parser.add_argument(
    '-sr',
    '--show_results',
    help='Show all results.',
    action='store_true'
)
parser.add_argument(
    '-g',
    '--gui',
    help='Show program with GUI.',
    action='store_true'
)

args = parser.parse_args()

if args.gui:
    appVM = MainViewModel(args.password, args.show_results)
    appVM.show_engien()
else:
    console_input.check_password(args.password, args.show_results)
