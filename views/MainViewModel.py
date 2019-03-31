#!/usr/bin/python3.7
# -*- encoding: utf-8 -*-

from PySide2.QtCore import QObject, Signal, Property, QUrl, Slot

from utils import password

class MainViewModel(QObject):
    textChanged = Signal(str)
    boolChanged = Signal(bool)

    def __init__(
        self,
        password: str=None,
        show_results: bool=False,
        parent: QObject=None
    ):
        QObject.__init__(self, parent)
        self.m_password = password
        self.m_show_results = show_results
        self.m_password_hash = '<leer>'
        self.m_result = '<leer>'

    def ViewFileName(self):
        return __file__.replace('Model.py', '') + '.qml'

    @Property(str, notify=textChanged)
    def password(self) -> str:
        return self.m_password

    @password.setter
    def setPassword(self, text: str) -> None:
        if self.m_password == text:
            return
        self.m_password = text
        self.textChanged.emit(self.m_password)

    @Property(str, notify=textChanged)
    def password_hash(self) -> str:
        return self.m_password_hash

    @password_hash.setter
    def setPassword_hash(self, text: str) -> None:
        if self.m_password_hash == text:
            return
        self.m_password_hash = text
        self.textChanged.emit(self.m_password_hash)


    @Property(bool, notify=boolChanged)
    def show_results(self) -> bool:
        return self.m_show_results

    @show_results.setter
    def setShow_results(self, value: bool) -> None:
        if self.m_show_results == value:
            return
        self.m_show_results = value
        self.boolChanged.emit(self.m_show_results)

    @Property(str, notify=textChanged)
    def result(self) -> bool:
        return self.m_result

    @result.setter
    def setResult(self, text: str) -> None:
        if self.m_result == text:
            return
        self.m_result = text
        self.textChanged.emit(self.m_result)

    @Slot()
    def apply(self):
        if not self.m_password:
            raise ValueError('Password must not be empty!')

        pwd = password.hash_str_password(self.m_password)
        self.setPassword_hash(pwd)

        finds = password.send_password_request(pwd)

        # if self.m_show_results:
            # ToDo: Write into list

        pwd_info = password.is_password_in_results(pwd, finds)
        if not pwd_info:
            print('Nothing found!')
            # ToDo: Write into label
        else:
            if self.m_show_results:
                self.setResult(f'pwd id: {pwd_info.pwd_id} count: {pwd_info.count}')
                # ToDo: Write into label
                # ToDo: Select list item and / or change color of list item.
            else:
                self.setResult(f'count: {pwd_info.count}')
                # ToDo: Write into label

        print()
