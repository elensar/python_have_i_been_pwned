#!/usr/bin/python3.7.1
# -*- encoding: utf-8 -*-

class password_info():
    """This is just a small class to store some information and to simplify some logic."""

    def __init__(self, pwd_id:int, pwd_prefix:str, pwd, count):
         self.pwd_id = pwd_id
         self.pwd_prefix = pwd_prefix
         self.password = self._convert_password(pwd_prefix, pwd)
         self.count = self._convert_count(count)

    def _convert_password(self, pwd_prefix, pwd):
        prefix = pwd_prefix.upper()
        if isinstance(pwd, str):
            return bytes(prefix + pwd.upper(), 'utf-8')
        elif isinstance(pwd, bytes):
            return bytes(prefix, 'utf-8') + pwd
        else:
            raise TypeError('"password" has wrong type. It must be a str or bytes!')

    def _convert_count(self, count):
        if isinstance(count, str):
            return int(count)
        elif isinstance(count, int):
            return count
        else:
            raise TypeError('"count" has wrong type. It must be a str or int!')

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.password == other.password
        elif isinstance(other, bytes):
            return self.password == other
        elif isinstance(other, str):
            return self.password == self._convert_password('', other)
        else:
            return False
