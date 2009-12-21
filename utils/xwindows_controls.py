from Xlib import X, display

###########################
## Configuracion de la posicion en la pila de ventanas
## http://tronche.com/gui/x/xlib/window/configure.html
############################

class MicroManager:
	def __init__(self):
		self.display = display.Display()
		
	def getWindows(self, screen_number = 0):
		win_map = {}
		root = self.display.screen(screen_number).root
		for window in root.query_tree().children:
			try:
				name = window.get_property(39,0,0,200000).value
				win_map[name] = window
			except:
				continue
		return win_map
		
	def toTop(self, window):
		window.configure(stack_mode=X.Above)
		self.display.sync()
		
	def toDesktop(self, window):
		window.configure(stack_mode=X.Below)	
		self.display.sync()
		
	def setDimensions(self, window, x, y, width, height):
		window.configure(x = x, y = y, width = width, height = height)
		self.display.sync()		
		
	def screenSize(self, screen_number = 0):
		screen = self.display.screen(screen_number)
		return (screen.width_in_pixels, screen.height_in_pixels) 

#############################
## identificacion de las ventanas de mediateca
#############################
class MediatecaWindows:
	video = None
	audio = None
	firefox = None
	tv = None
	mixer = None

import re

def select_mediateca_windows(win_dict):
	desired_windows = MediatecaWindows()
	for i,j in win_dict.iteritems():
		if i.startswith("VLC"):
			desired_windows.video = j
		if re.match(".*Sonata.*", i) != None:
			desired_windows.audio = j
		if i.endswith("Mozilla Firefox"):
			desired_windows.firefox = j
		if i.startswith("tvtime"):
			desired_windows.tv = j
		if i.startswith("Volume Control"):
			desired_windows.mixer = j	

	return desired_windows
