#!/usr/bin/python3.7
# -*- encoding: utf-8 -*-

from sys import stdin
from utils import password

def check_password(pre_pwd: str, show_results: bool=False):
    pwd_input = ''
    if pre_pwd:
        pwd_input = pre_pwd
    else:
        print('Please enter your password:')

        # rstrip remove just the trailing chars which will be \n
        # because the user has to enter to continue the check.
        pwd_input = stdin.readline().rstrip('\n')

    pwd = password.hash_str_password(pwd_input)

    print(pwd)
    print()

    finds = password.send_password_request(pwd)

    if show_results:
        print('Results:')
        for item in finds:
            print(f'{item.pwd_id:3d} - {item.password}: finds: {item.count:4d}')

        print()

    pwd_info = password.is_password_in_results(pwd, finds)
    if not pwd_info:
        print('Nothing found!')
    else:
        if show_results:
            print(f'pwd id: {pwd_info.pwd_id} count: {pwd_info.count}')
        else:
            print(f'count: {pwd_info.count}')
