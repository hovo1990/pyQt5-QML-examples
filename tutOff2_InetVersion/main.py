# -*- coding: utf-8 -*-

try:
    from PySide import QtCore
    from PySide import QtWidgets
except:
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets

try:
    from PyQt5.QtGui import QPainter
    from PyQt5.QtWidgets import QStyleOptionGraphicsItem
    from PyQt5.QtWidgets import QWidget
    from PyQt5.QtWidgets import QGraphicsItem

    from PyQt5.QtQuick import QQuickItem
    from PyQt5.QtQuick import QQuickPaintedItem
except Exception as e:
    print("Error in importing modules ",e)

class PaintedItem(QQuickPaintedItem):
    def __init__(self, parent = None):
        super(PaintedItem, self).__init__(parent)
#        self.setFlag(QQuickItem.ItemHasContents, False)
#        print("What the fuck")

    def paint(self, painter):
        painter.fillRect(self.contentsBoundingRect(), Qt.red);
        print("damn")
#        painter.save()

#        painter.setPen(Qt.red)
#        painter.drawEllipse(opts.rect)

#        painter.restore()




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



