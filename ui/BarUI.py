# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bar.ui'
#
# Created: Sat Dec 19 06:56:12 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(150, 800)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(133, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Frame.setPalette(palette)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.audio = QtGui.QToolButton(Frame)
        self.audio.setGeometry(QtCore.QRect(0, 0, 150, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/A/Music Player 4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio.setIcon(icon)
        self.audio.setIconSize(QtCore.QSize(150, 150))
        self.audio.setAutoRepeat(False)
        self.audio.setObjectName("audio")
        self.mail = QtGui.QToolButton(Frame)
        self.mail.setGeometry(QtCore.QRect(0, 300, 150, 150))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/A/eMail.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mail.setIcon(icon1)
        self.mail.setIconSize(QtCore.QSize(150, 150))
        self.mail.setAutoRepeat(False)
        self.mail.setObjectName("mail")
        self.video = QtGui.QToolButton(Frame)
        self.video.setGeometry(QtCore.QRect(0, 150, 150, 150))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/A/Video 2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.video.setIcon(icon2)
        self.video.setIconSize(QtCore.QSize(150, 150))
        self.video.setAutoRepeat(False)
        self.video.setObjectName("video")
        self.internet = QtGui.QToolButton(Frame)
        self.internet.setGeometry(QtCore.QRect(0, 450, 150, 150))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/A/Internet.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.internet.setIcon(icon3)
        self.internet.setIconSize(QtCore.QSize(150, 150))
        self.internet.setAutoRepeat(False)
        self.internet.setObjectName("internet")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.audio.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mail.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.video.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.internet.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))

import Icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

