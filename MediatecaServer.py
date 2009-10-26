## configuracion dependiente del SO
import platform

uname = platform.system() 

if uname == "Windows":
    from pyvlc import vlc
elif uname == "Linux":
    import vlc

## gestion de archivos
from os.path import exists

##serializacion
from ctypes import *
import struct

from video_base import VideoBase

#import pygst
#pygst.require("0.10")
#import gst

## comunicaciones
import socket_rpc.server as socket_rpc
import bt_rpc.server as bt_rpc

## constantes identificadoras de operacion
from op_constants import *

class MediatecaServer:

  def __init__(self, port = 16667):
    self.active = True
    self.video_base = VideoBase("/media/archivo_general/Mediateca/Video")
    self.media_control = vlc.MediaControl(["--video-x","600","--video-y","50", "--width", "640", "--height","480"])
    #self.audio_control = gst.element_factory_make("playbin", "player")
    #self.audio_control.set_property("uri", "file://" + "/media/archivo_general/Mediateca/Audio/coleccion/Amy Mcdonald - This Is The Life.mp3")
    #self.audio_control.set_state(gst.STATE_PLAYING)

    self.playlist = self.video_base.getPlaylistAll()
    
    ### endpoint-servidor de comunicaciones
    ## Socket AF_INET, TCP
    self.rpc = socket_rpc.RPCServer(port)
    
    ### DICCIONARIO DE OPERACIONES
    self.rpc.setOp(MIRROR, self.mirror)
    self.rpc.setOp(NEXT_VIDEO, self.nextVideo)
    self.rpc.setOp(PREV_VIDEO, self.prevVideo)
    self.rpc.setOp(PAUSE, self.pause)
    self.rpc.setOp(PLAY, self.play)
    self.rpc.setOp(ADVANCE, self.advance)
    self.rpc.setOp(REWIND, self.rewind)
    self.rpc.setOp(JUMP_TO, self.jumpTo)
    self.rpc.setOp(FULLSCREEN, self.fullscreen)
    self.rpc.setOp(GET_PLAYLIST, self.getPlaylist)
    self.rpc.setOp(SORT, self.sort)
    self.rpc.setOp(LENGTH, self.length)
    self.rpc.setOp(STOP, self.stop)
    self.rpc.setOp(GET_POS, self.getPos)
    self.rpc.setOp(SET_POS, self.setPos)
    self.rpc.setOp(RELOAD, self.reload)
    self.rpc.setOp(ADD_FROM_DIR, self.addFromDir)
    
    self.rpc.start()
    
    ### endpoint-servidor de comunicaciones
    ## Bluetooth RFCOMM
    self.bt_rpc = bt_rpc.RPCServer(port+2)
    
    ### DICCIONARIO DE OPERACIONES
    self.bt_rpc.setOp(MIRROR, self.mirror)
    self.bt_rpc.setOp(NEXT_VIDEO, self.nextVideo)
    self.bt_rpc.setOp(PREV_VIDEO, self.prevVideo)
    self.bt_rpc.setOp(PAUSE, self.pause)
    self.bt_rpc.setOp(PLAY, self.play)
    self.bt_rpc.setOp(ADVANCE, self.advance)
    self.bt_rpc.setOp(REWIND, self.rewind)
    self.bt_rpc.setOp(JUMP_TO, self.jumpTo)
    self.bt_rpc.setOp(FULLSCREEN, self.fullscreen)
    self.bt_rpc.setOp(GET_PLAYLIST, self.getPlaylist)
    self.bt_rpc.setOp(SORT, self.sort)
    self.bt_rpc.setOp(LENGTH, self.length)
    self.bt_rpc.setOp(STOP, self.stop)
    self.bt_rpc.setOp(GET_POS, self.getPos)
    self.bt_rpc.setOp(SET_POS, self.setPos)
    self.bt_rpc.setOp(RELOAD, self.reload)
    self.bt_rpc.setOp(ADD_FROM_DIR, self.addFromDir)
    
    self.bt_rpc.start()
    
  def mirror(self, clisk, data):
    return (1, data)
    
  def nextVideo(self, clisk, data):
    self.media_control.stop()
    nn = self.playlist.next()
    
    if nn is None:
        return (0,"not exists")
    
    self.media_control.set_mrl(nn)
    self.media_control.start()
    return (1, nn)
    
  def reload(self, clisk, data):
    self.playlist = self.video_base.getPlaylistAll()
    return (1, None)
    
  def prevVideo(self, clisk, data):
    self.media_control.stop()
    pv = self.playlist.prev()
    
    if pv is None:
        return (0,"not exists")
        
    self.media_control.set_mrl(pv)
    self.media_control.start()
    return (1, pv)
    
  def jumpTo(self, clisk, data):
    pos = struct.unpack("!h",data)[0]
    if pos >= self.playlist.count():
        return (0,"not exists")
    else:
        jp = self.playlist.get(pos)
        self.media_control.stop()
        self.media_control.set_mrl(jp)
        self.media_control.start()
        return (1, jp)
    
  def pause(self, clisk, data):
    self.media_control.pause()
    return (1, None)
    
  def play(self, clisk, data):
    self.media_control.resume()
    return (1, None)
    
  def advance(self, clisk, data):
    pos = self.media_control.get_media_position(0,0)
    pos.value += 5000
    self.media_control.set_media_position(pos)
    
    return (1,pos.value)
    
  def rewind(self, clisk, data):
    pos = self.media_control.get_media_position(0,0)
    pos.value -= 5000
    self.media_control.set_media_position(pos)
    
    return (1,pos.value)
    
  def fullscreen(self, clisk, data):
    self.media_control.set_fullscreen(1)
    
    return (1,None)
    
  def getPlaylist(self, clisk, data):
    start, end = struct.unpack("!ii",data)
    return (1, self.playlist.ls()[start: end])
    
  def sort(self, clisk, data):
    self.playlist.sort()
    return (1, None)
    
  def length(self, clisk, data):
    return (1, self.playlist.count())
    
  def stop(self, clisk, data):
    self.rpc.active = False
    self.bt_rpc.active = False
    return (1, None)
    
  def getPos(self, clisk, data):
    pos = self.media_control.get_media_position(0,0)
    return (1, pos.value)
        
  def setPos(self, clisk, data):
    pos = struct.unpack("!i",data)[0]
    self.media_control.set_media_position(pos)
    return (1, None)    

  def addFromDir(self, clisk, data):
    len = struct.unpack("!i",data[:sizeof(c_int)])[0]
    dir = data[sizeof(c_int):len+sizeof(c_int)].encode("utf-8")
    if exists(dir):
      self.playlist.addFromDir(dir)
      return (1, None)
    else:
      return (0, "Directory not found")
    
  def security(self, clisk, address):
    return True
