# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bar.ui'
#
# Created: Tue Dec 22 01:58:28 2009
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
        self.mail.setIconSize(QtCore.QSize(128, 128))
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
        self.mixer = QtGui.QToolButton(Frame)
        self.mixer.setGeometry(QtCore.QRect(0, 600, 71, 71))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/A/Delete.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mixer.setIcon(icon4)
        self.mixer.setIconSize(QtCore.QSize(48, 48))
        self.mixer.setObjectName("mixer")
        self.cd_writer = QtGui.QToolButton(Frame)
        self.cd_writer.setGeometry(QtCore.QRect(80, 600, 71, 71))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/A/CD.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cd_writer.setIcon(icon5)
        self.cd_writer.setIconSize(QtCore.QSize(64, 64))
        self.cd_writer.setObjectName("cd_writer")
        self.terminal = QtGui.QToolButton(Frame)
        self.terminal.setGeometry(QtCore.QRect(0, 670, 71, 71))
        self.terminal.setObjectName("terminal")
        self.tv = QtGui.QToolButton(Frame)
        self.tv.setGeometry(QtCore.QRect(80, 670, 71, 71))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/A/tve1logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tv.setIcon(icon6)
        self.tv.setIconSize(QtCore.QSize(32, 32))
        self.tv.setObjectName("tv")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.audio.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mail.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.video.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.internet.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mixer.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cd_writer.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.terminal.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tv.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))

import Icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

