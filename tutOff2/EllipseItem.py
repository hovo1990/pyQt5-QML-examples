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

class EllipseItem(QQuickPaintedItem):
    def __init__(self, parent = None):
        super(EllipseItem, self).__init__(parent)
        self.setFlag(QQuickItem.ItemHasContents, False)
#        print("What the fuck")

#    def paintEvent(self,e):
#        print('yolo')

    def paint(self, painter, opts):
        print("damn")
        painter.save()

        painter.setPen(Qt.red)
        painter.drawEllipse(opts.rect)

        painter.restore()
