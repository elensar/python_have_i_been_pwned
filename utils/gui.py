#!/usr/bin/python3.7
# -*- encoding: utf-8 -*-

import sys

from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from views.MainViewModel import MainViewModel

def showEngine(appVM: MainViewModel=None):
    if not appVM:
        appVM = MainViewModel()

    viewFile = appVM.ViewFileName()
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("appVM", appVM)
    engine.load(QUrl.fromLocalFile(viewFile))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
