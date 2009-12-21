from popen2 import popen2

from ui.BarUI import Ui_Frame

from PyQt4 import QtCore, QtGui

from utils.xwindows_controls import MicroManager, select_mediateca_windows, X

class ControlBar(QtGui.QFrame):
	def __init__(self,parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QFrame.__init__(self, parent, f)
		
		self.ui = Ui_Frame()
		self.ui.setupUi(self)
		
		self.wm = MicroManager()
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		
		self.current = None
		self.width, self.height = self.wm.screenSize()
		
		QtCore.QObject.connect (self.ui.audio, QtCore.SIGNAL ("clicked()"), self.showAudio)
		QtCore.QObject.connect (self.ui.video, QtCore.SIGNAL ("clicked()"), self.showVideo)
		QtCore.QObject.connect (self.ui.internet, QtCore.SIGNAL ("clicked()"), self.showInternet)
		QtCore.QObject.connect (self.ui.mail, QtCore.SIGNAL ("clicked()"), self.showMixer)

		end = 0

	def showAudio(self):
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		self.wm.setDimensions(self.windows.audio, 150, 0, self.width - 150, self.height)
		self.wm.toTop(self.windows.audio)
		self.windows.audio.set_input_focus(X.RevertToNone, 0)
		
	def showVideo(self):
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		if self.windows.tv is None:
			popen2("tvtime-sound")
		while self.windows.tv is None:
			allwin = self.wm.getWindows()
			self.windows = select_mediateca_windows(allwin)
		x,y,w,h = self.wm.getDimensions(self.windows.tv)
		while x!=150 or y!=0 or w!=self.width-150 or h!=self.height:
			self.wm.setDimensions(self.windows.tv, 150, 0, self.width - 150, self.height)
			x,y,w,h = self.wm.getDimensions(self.windows.tv)

		self.wm.toTop(self.windows.tv)		
		self.windows.tv.set_input_focus(X.RevertToNone, 0)
		
	def showInternet(self):
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		if self.windows.firefox is None:
			popen2("firefox")
		while self.windows.firefox is None:
			allwin = self.wm.getWindows()
			self.windows = select_mediateca_windows(allwin)
		x,y,w,h = self.wm.getDimensions(self.windows.firefox)
		while x!=150 or y!=0 or w!=self.width-150 or h!=self.height:
			self.wm.setDimensions(self.windows.firefox, 150, 0, self.width - 150, self.height)
			x,y,w,h = self.wm.getDimensions(self.windows.firefox)

		self.wm.toTop(self.windows.firefox)		
		self.windows.firefox.set_input_focus(X.RevertToNone, 0)
	
	def showMixer(self):
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		self.wm.setDimensions(self.windows.mixer, 150, 0, self.width - 150, self.height)
		self.wm.toTop(self.windows.mixer)
		self.windows.mixer.set_input_focus(X.RevertToNone, 0)
		
	def verifyWindowSizes(self):
		end = 0
		while end != 1:
				allwin = self.wm.getWindows()
				self.windows = select_mediateca_windows(allwin)
				
				end = 1
				for win in [self.windows.audio, self.windows.firefox, self.windows.mixer]:
					if win is None:
						end = 0
					else:
						x,y,w,h = self.wm.getDimensions(win)
						if x != 150 or y !=0 or w != self.width - 150 or h != self.height:
							self.wm.setDimensions(win, 150, 0, self.width - 150, self.height)
							end = 0
	
from time import sleep
from exceptions import Exception
		
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = ControlBar()
    Frame.show()
    Frame.verifyWindowSizes()
    Frame.showVideo()
    sys.exit(app.exec_())
