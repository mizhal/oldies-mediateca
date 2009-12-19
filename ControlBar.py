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
		
		end = 0

	def showAudio(self):
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		self.wm.setDimensions(self.windows.audio, 150, 0, 
																						self.width - 150, self.height)
		self.wm.toTop(self.windows.audio)
		self.windows.audio.set_input_focus(X.RevertToNone, 0)
		
	def showVideo(self):
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		self.wm.setDimensions(self.windows.video, 150, 0, 
																						self.width - 150, self.height)
		self.wm.toTop(self.windows.video)		
		self.windows.video.set_input_focus(X.RevertToNone, 0)
		
	def showInternet(self):
		allwin = self.wm.getWindows()
		self.windows = select_mediateca_windows(allwin)
		self.wm.setDimensions(self.windows.firefox, 150, 0, 
																						self.width - 150, self.height)
		self.wm.toTop(self.windows.firefox)		
		self.windows.firefox.set_input_focus(X.RevertToNone, 0)
		
from time import sleep
		
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = ControlBar()
    Frame.show()

    end = 0
    while end != 1: 
    	try:
    		Frame.showAudio()
    		Frame.showInternet()
    		sleep(1)
    		end = 1
    	except:
    		pass

    sys.exit(app.exec_())