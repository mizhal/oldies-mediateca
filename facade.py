from os.path import join, exists

from readini import IniFile

class Mediateca:
	subsystem_dir = join("/",*__file__.split("/")[:-1])
	config = IniFile(join(subsystem_dir, "config.ini"))
	
	def __init__(self):
		'''ensamblado de todos los componentes
		de acuerdo a la configuracion'''
	
class ControllerMap:
	'''Componente que de media center '''
	
	def __init__(self, remote_controls, engine):
		self.controls = remote_controls
		self.engine = engine
		
		## enrutamiento de comandos
		for rpc in remote_controls:
			### DICCIONARIO DE OPERACIONES
			rpc.setOp(MIRROR, engine.mirror)
			rpc.setOp(NEXT_VIDEO, engine.nextVideo)
			rpc.setOp(PREV_VIDEO, engine.prevVideo)
			rpc.setOp(PAUSE, engine.pause)
			rpc.setOp(PLAY, engine.play)
			rpc.setOp(ADVANCE, engine.advance)
			rpc.setOp(REWIND, engine.rewind)
			rpc.setOp(JUMP_TO, engine.jumpTo)
			rpc.setOp(FULLSCREEN, engine.fullscreen)
			rpc.setOp(GET_PLAYLIST, engine.getPlaylist)
			rpc.setOp(SORT, engine.sort)
			rpc.setOp(LENGTH, engine.length)
			rpc.setOp(SHUTDOWN, engine.stop)
			rpc.setOp(GET_POS, engine.getPos)
			rpc.setOp(SET_POS, engine.setPos)
			rpc.setOp(RELOAD, engine.reload)
			rpc.setOp(ADD_FROM_DIR, engine.addFromDir)
			rpc.setOp(STREAM_LENGTH, engine.streamLength)
			rpc.setOp(SELECT, engine.selectActiveEngine)
			
			rpc.start()
