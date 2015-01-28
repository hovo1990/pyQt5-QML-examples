#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
## -*- coding: utf-8 -*-
## -*- coding: utf-8 -*-
#import sys
#from PyQt5.QtCore import QObject, QUrl, Qt
#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtQml import QQmlApplicationEngine

##THis fucking works mate



import sys
import os.path

from PyQt5.QtCore import QObject,  Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
import myQML

app = QGuiApplication(sys.argv)



print('-----------------------------------------------------------------------')


qmlFile = 'main.qml'

#qmlFile = "qrc:data/"


view = QQuickView()
view.setResizeMode(QQuickView.SizeRootObjectToView)
view.engine().quit.connect(app.quit)

engine = view.engine()
view.setSource(QUrl(qmlFile)) # putting at the end didn't solve referenceError 'This is supposed to solve all referenceErrors



view.show()
sys.exit(app.exec_())


