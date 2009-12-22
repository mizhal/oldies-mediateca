from popen2 import popen2
import weakref
import re

from ui.BarUI import Ui_Frame

from PyQt4 import QtCore, QtGui

from utils.xwindows_controls import MicroManager, X

class ControlBar(QtGui.QFrame):
	def __init__(self,parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QFrame.__init__(self, parent, f)
		
		self.ui = Ui_Frame()
		self.ui.setupUi(self)
		
		self.wm = MicroManager()
		
		self.current = None
		self.width, self.height = self.wm.screenSize()
		
		QtCore.QObject.connect (self.ui.audio, QtCore.SIGNAL ("clicked()"), self.showAudio)
		QtCore.QObject.connect (self.ui.video, QtCore.SIGNAL ("clicked()"), self.showVideo)
		QtCore.QObject.connect (self.ui.internet, QtCore.SIGNAL ("clicked()"), self.showInternet)
		QtCore.QObject.connect (self.ui.mixer, QtCore.SIGNAL ("clicked()"), self.showMixer)
		QtCore.QObject.connect (self.ui.terminal, QtCore.SIGNAL ("clicked()"), self.showTerminal)
		QtCore.QObject.connect (self.ui.cd_writer, QtCore.SIGNAL ("clicked()"), self.showCDWriter)

		end = 0
		
		self._pages_cache = weakref.WeakValueDictionary()
		
	def _showAsPage(self, name, win_match_fun, executable):

		if not self._pages_cache.has_key(name):
			for name, window in self.wm.getWindows().iteritems():
				if win_match_fun(name):
					self._pages_cache[name] = window
					break
		
		winpage = self._pages_cache.get(name, None)
				
		if winpage is None:
			if executable is None:
				return
			else:
				popen2(executable)
		while winpage is None:
			for name, window in self.wm.getWindows().iteritems():
				if win_match_fun(name):
					winpage = window
					self._pages_cache[name] = window
					break
					
		x,y,w,h = self.wm.getDimensions(winpage)
		while x!=150 or y!=0 or w!=self.width-150 or h!=self.height:
			self.wm.setDimensions(winpage, 150, 0, self.width - 150, self.height)
			x,y,w,h = self.wm.getDimensions(winpage)

		self.wm.toTop(winpage)		
		winpage.set_input_focus(X.RevertToNone, 0)
		
	def showVideo(self):
		win_match = lambda name: name.startswith("VLC")
		self._showAsPage('video',win_match, None)
		
	def showAudio(self):
		win_match = lambda name: re.match(".*Sonata.*", name) != None
		self._showAsPage('audio',win_match, "sonata")
		
	def showTV(self):
		win_match = lambda name: name.startswith("tvtime")
		self._showAsPage('tv',win_match, "tvtime")
		
	def showInternet(self):
		win_match = lambda name: name.endswith("Mozilla Firefox")
		self._showAsPage('internet',win_match, "firefox")
	
	def showMixer(self):
		win_match = lambda name: name.startswith("Volume Control")
		self._showAsPage('mixer',win_match, "pavucontrol")

	def showCDWriter(self):
		win_match = lambda name: name.startswith("Brasero")
		self._showAsPage('cd_writer',win_match, "brasero")
		
	def showTerminal(self):
		win_match = lambda name: name.startswith("mediateca-terminal")
		self._showAsPage('terminal',win_match, 'xterm -T "mediateca-terminal" -fg white -bg black')
	
from time import sleep
from exceptions import Exception
		
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = ControlBar()
    Frame.show()
    #Frame.verifyWindowSizes()
    #Frame.showVideo()
    sys.exit(app.exec_())
