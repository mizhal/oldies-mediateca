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
		
	def getClasses(self, screen_number = 0):
		win_map = {}
		root = self.display.screen(screen_number).root
		for window in root.query_tree().children:
			try:
				name = window.get_wm_class()
				win_map.setdefault(name, [])
				win_map[name].append(window)
			except:
				continue
		return win_map		
		
	def toTop(self, window):
		if not isinstance(window, list):
			wlist = [window]
		else:
			wlist = window
		for window in wlist:
			window.configure(stack_mode=X.Above)
		self.display.sync()
		
	def toDesktop(self, window):
		if not isinstance(window, list):
			wlist = [window]
		else:
			wlist = window
		for window in wlist:
			window.configure(stack_mode=X.Below)	
		self.display.sync()

	def focus(self, window):
		if not isinstance(window, list):
			wlist = [window]
		else:
			wlist = window
		for window in wlist:
			window.set_input_focus(X.PointerRoot,X.CurrentTime)
		self.display.sync()

	def setDimensions(self, window, x, y, width, height):
		if not isinstance(window, list):
			wlist = [window]
		else:
			wlist = window
		for window in wlist:
			try:
				window.configure(x = x, y = y, width = width, height = height)
			except:
				continue
		self.display.sync()		
		
	def getDimensions(self, window):
		'''returns (x, y, width, height)'''
		geom = window.get_geometry()
		return (geom.x, geom.y, geom.width, geom.height)
		
	def screenSize(self, screen_number = 0):
		screen = self.display.screen(screen_number)
		return (screen.width_in_pixels, screen.height_in_pixels)
