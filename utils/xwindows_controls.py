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
		
	def getDimensions(self, window):
		'''returns (x, y, width, height)'''
		geom = window.get_geometry()
		return (geom.x, geom.y, geom.width, geom.height)
		
	def screenSize(self, screen_number = 0):
		screen = self.display.screen(screen_number)
		return (screen.width_in_pixels, screen.height_in_pixels)
