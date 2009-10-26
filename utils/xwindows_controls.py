def getWindows(display):
	win_map = {}
	root = display.screen().root
	for window in root.query_tree().children:
		try:
			name = window.get_property(39,0,0,200000).value
			win_map[name] = window
		except:
			continue
	return win_map
	
###########################
## Configuracion de la posicion en la pila de ventanas
## http://tronche.com/gui/x/xlib/window/configure.html
############################

def toTop(window):
	window.configure(stack_mode=X.Above)
	display.sync()
	
def toDesktop(window):
	window.configure(stack_mode=X.Below)	
	display.sync()