#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from os.path import split

from math import floor
from time import sleep
from threading import Thread

from PyQt4 import QtGui, QtCore

from mediateca.MediatecaClient import MediatecaClient

from ui.Remote import Ui_Frame

class Stream:
	length = 0
	title = u''

class Remote(Thread):
	def __init__(self):
		Thread.__init__(self)
		
		self.link = MediatecaClient("192.168.6.1",16667)
		self.window = QtGui.QFrame()
		self.ui = Ui_Frame()
		self.ui.setupUi(self.window)
		
		QtCore.QObject.connect (self.ui.play, QtCore.SIGNAL ("clicked()"), self.playControl)
		QtCore.QObject.connect (self.ui.next, QtCore.SIGNAL ("clicked()"), self.next)
		QtCore.QObject.connect (self.ui.previous, QtCore.SIGNAL ("clicked()"), self.prev)
		QtCore.QObject.connect (self.ui.fullscreen, QtCore.SIGNAL ("clicked()"), self.fullscreen)
		QtCore.QObject.connect (self.ui.load_cd, QtCore.SIGNAL ("clicked()"), self.loadFromCD)
		QtCore.QObject.connect (self.ui.list, QtCore.SIGNAL ("itemDoubleClicked(QListWidgetItem *)"), self.jump)
		QtCore.QObject.connect (self.ui.slider, QtCore.SIGNAL ("sliderReleased()"), self.setPosition)
		QtCore.QObject.connect (self.ui.filter, QtCore.SIGNAL ("textChanged (const QString&)"), self.filter)


		self.playlist = []
		
		self.refreshPlaylist()
		
		self.current = Stream()
		
		self.playing = False
		
	def run(self):
		robin = 0
		while 1:
			if False and robin % 60 ==0:
				self.refreshPlaylist()
				robin = 0
			self.refreshPosition()
			robin += 1
			sleep(1)

	def updateCurrent(self, title):
		self.playing = True
		self.current.title = split(title)[1]
		self.current.length = self.link.getStreamLength()
		
	def updateUI(self):
		self.ui.current.setText(self.current.title)
		self.ui.slider.setValue(0)
		
	def refreshPosition(self):
		position = self.link.getPosition()
		length = self.link.getStreamLength()
		if not position is None and not length is None:
			percent = 100*float(position)/length
			self.ui.slider.setValue(floor(percent))
	
	def refreshPlaylist(self):
		self.ui.list.clear()
		
		playlist_length = self.link.playlistLength()
		
		counter = 0
		for i in range(playlist_length/50 + 1):
			for media in self.link.playlist(i*50, (i+1)*50):
				lvi = QtGui.QListWidgetItem(self.ui.list)
				lvi.setData(QtCore.Qt.UserRole, counter)
				lvi.setText(media)
				
				self.playlist.append((media,counter))
					
				counter += 1
				
	def filter(self, text):
		filter_RE = re.compile(".*%s.*"%text.toLower())
		
		self.ui.list.clear()
		
		for media, counter in self.playlist:
			if filter_RE.match(media.lower()):
				lvi = QtGui.QListWidgetItem(self.ui.list)
				lvi.setData(QtCore.Qt.UserRole, counter)
				lvi.setText(media)
				
	def show(self):
		self.window.show()
		
	def playControl(self):
		if self.playing:
			self.link.pause()
		else:
			self.link.resume()
		
	def pause(self):
		self.link.pause()

	def loadFromCD(self):
		self.link.addFromDir("/media/cdrom")
		
	def next(self):
		self.updateCurrent(self.link.next())
		self.updateUI()
		
	def prev(self):
		self.updateCurrent(self.link.prev())
		self.updateUI()
		
	def jump(self):
		row = self.ui.list.currentRow()
		item = self.ui.list.item(row)
		value, validation = item.data(QtCore.Qt.UserRole).toInt()
		playing = self.link.jumpTo(value)
		self.updateCurrent(playing)
		self.updateUI()

	def setPosition(self):
		percent = self.ui.slider.value()/100.0
		self.link.setPosition(self.link.getStreamLength() * percent)
		
	def fullscreen(self):
		self.link.fullscreen()
		

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    remote = Remote()
    remote.start()
    remote.show()
    sys.exit(app.exec_())