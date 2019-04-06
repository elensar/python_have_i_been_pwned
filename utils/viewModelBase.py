#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import sys

from PySide2.QtCore import QObject, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

class ViewModelBase(QObject):

    def __init__(
        self,
        parent: QObject=None
    ):
        QObject.__init__(self, parent)

    def get_file_name(self):
        return __file__

    def view_file_name(self):
        return self.get_file_name().replace('Model.py', '') + '.qml'

    def show_engien(self):
        viewFile = self.view_file_name()
        app = QGuiApplication(sys.argv)

        engine = QQmlApplicationEngine()
        engine.rootContext().setContextProperty("appVM", self)
        engine.load(QUrl.fromLocalFile(viewFile))

        if not engine.rootObjects():
            sys.exit(-1)

        sys.exit(app.exec_())
