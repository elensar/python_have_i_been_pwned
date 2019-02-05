#!/usr/bin/python3.7.1
# -*- encoding: utf-8 -*-

import hashlib
from utils import web_request
from utils.password_info import password_info

PWD_PREFIX_LEN = 5

def hash_str_password(password:str) -> str:
    pwd_bytes = bytes(password, 'utf-8')
    return hash_bytes_password(pwd_bytes)

def hash_bytes_password(password:bytes) -> str:
    new_sha1 = hashlib.sha1()
    new_sha1.update(password)
    return new_sha1.hexdigest()

def send_password_request(hashed_pwd:str):
    pwd_prefix = hashed_pwd[:PWD_PREFIX_LEN]
    return web_request.send_password_request(pwd_prefix)

def is_password_in_results(password:str, finds) -> password_info:
    for item in finds:
        if item.__eq__(password):
            return item

    return None
