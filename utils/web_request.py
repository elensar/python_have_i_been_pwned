#!/usr/bin/python3.7
# -*- encoding: utf-8 -*-

import urllib3
from typing import Iterable
from utils.password_info import password_info

PWND_API_URL = 'https://api.pwnedpasswords.com/range/{0}'

def send_password_request(pwd_prefix:str) -> Iterable[password_info]:
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    response = http.request('GET', PWND_API_URL.format(pwd_prefix))

    if response.status != 200:
        raise Exception()

    data = response.data.decode('utf-8')
    lines = data.splitlines()

    pwd_id = 0
    result = []
    for line in lines:
        pwd_id += 1
        d = line.split(':')
        result.append( password_info(pwd_id, pwd_prefix, d[0], d[1]) )

    return result
