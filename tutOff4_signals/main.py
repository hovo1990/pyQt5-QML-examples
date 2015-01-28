#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

try:
    from PySide import QtCore
    from PySide import QtWidgets
except:
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets

try:
    from PyQt5.QtQuick import QQuickPaintedItem
    from PyQt5.QtCore import (pyqtProperty, pyqtSignal, Q_CLASSINFO, QCoreApplication, QDate, QObject, QTime, QUrl)
    from PyQt5.QtCore import QTimerEvent
    from PyQt5.QtCore import QTimer

    from PyQt5.QtCore import qDebug
    from PyQt5.QtGui import QPainter
    from PyQt5.QtWidgets import QStyleOptionGraphicsItem
    from PyQt5.QtWidgets import QWidget
    from PyQt5.QtWidgets import QGraphicsItem

    from PyQt5.QtQuick import QQuickItem
    from PyQt5.QtCore import pyqtProperty
except Exception as e:
    print("Error in importing modules ",e)




class PaintedItem(QQuickPaintedItem):



    colorChanged = pyqtSignal()
    readyChanged = pyqtSignal(int)
    readySignal = pyqtSignal()
    #timerEvent

    def __init__(self, parent = None):
        super(PaintedItem, self).__init__(parent)
#        self.setFlag(QQuickItem.ItemHasContents, False)
#        print("What the fuck")
        self._color = Qt.red

#        timer = QTimer(self)
#        timer.timeout.connect(self.update)
#        timer.start(100)
        self.ready = 0
        self.startTimer(100)


    def timerEvent(self, timer):
        if self.ready >= 100:
            self.killTimer(timer.timerId())
#            qDebug(self.readySignal)<<"readySignal"
            print("Ready Signal called")
            self.readySignal.emit()
        else:
            self.ready += 1
            print('yo ',self.ready)
#            qDebug(self.readyChanged)
            self.readyChanged.emit(self.ready)

    def getReadyNumber(self):
        return self.ready

#    @pyqtProperty("QColor", fget = color, fset = setColor, notify = colorChanged)
    def getColor(self):
        return self._color

#    @color.setter
    def setColor(self,color):
        if self._color != color:
            self._color = color
            self.colorChanged.emit()
            self.update()



    def paint(self, painter):
        painter.fillRect(self.contentsBoundingRect(), self._color);
        print("damn")

    #THis fucking works yeah !!!!!!
    color = pyqtProperty("QColor", fget=getColor, fset= setColor, notify=colorChanged)
    value = pyqtProperty(int, fget=getReadyNumber, notify=readyChanged)



import sys
import os.path

from PyQt5.QtCore import QObject,  Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

#from EllipseItem import *

#import myQML

app = QGuiApplication(sys.argv)

qmlRegisterType(PaintedItem, 'mymodule', 1, 0, 'PaintedItem')

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



