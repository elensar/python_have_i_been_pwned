#!/usr/bin/python3.7
# -*- encoding: utf-8 -*-

import argparse
from views import console_input

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
    type=bool,
    default=False
)

args = parser.parse_args()
console_input.check_password(args.password, args.show_results)
