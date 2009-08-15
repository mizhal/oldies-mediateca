import socket
import struct
import simplejson
from threading import Thread
from select import select

from video_base import VideoBase
import vlc

import pygst
pygst.require("0.10")
import gst

from ctypes import *
from os.path import exists

#STATUS: Servidor RPC para controlar VLC en holofonor con multiclientes 

import zipfile

class MediatecaServer(Thread):
  ''' little rpc server for controlling
    holofonor '''
  
  def __init__(self, port = 16667):
    self.port = port
    self.active = True
    self.video_base = VideoBase("/media/archivo_general/Mediateca/Video")
    self.media_control = vlc.MediaControl(["--video-x","600","--video-y","50", "--width", "640", "--height","480"]) ## @todo calcular los valores de la posicion de la ventana X11 de vlc respecto de la resolucion de pantalla
    #self.audio_control = gst.element_factory_make("playbin", "player")
    #self.audio_control.set_property("uri", "file://" + "/media/archivo_general/Mediateca/Audio/coleccion/Amy Mcdonald - This Is The Life.mp3")
    #self.audio_control.set_state(gst.STATE_PLAYING)

    self.playlist = self.video_base.getPlaylistAll()
    
    self.operations = {
    0: self.mirror,
    1: self.nextVideo,
    2: self.prevVideo,
    3: self.pause,
    4: self.play,
    5: self.advance,
    6: self.rewind,
    7: self.jumpTo,
    8: self.fullscreen,
    9: self.getPlaylist,
    10: self.sort,
    11: self.length,
    12: self.stop,
    13: self.getPos,
    14: self.setPos,
    15: self.reload,
    16: self.addFromDir
    }
    
    Thread.__init__(self)
    
  def run(self):
    servsk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servsk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servsk.bind(("", self.port))
    servsk.listen(10)
    
    clisk = None
    addr = None
    devnull = None
    devnull2 = None
    incoming = [servsk]
    
    while self.active:
      ok_incoming, devnull, devnull2 = select(incoming, [], [], 2)
      
      if servsk in ok_incoming:      
        clisk, addr = servsk.accept()
        if(self.security(clisk, addr)):
          incoming.append(clisk)
        else:
          clisk.send(struct.pack("!hh",0,len("unauthorized"))+"unauthorized")
          clisk.close()
        
      clients = [sk for sk in ok_incoming if sk != servsk]
      for clisk in clients:
        header = None
        data = None
        try:
          header = clisk.recv(4)
          if len(header) > 0:
            msgid, datalen = struct.unpack("!hh",header)
            data = None
            if datalen:
              data = clisk.recv(datalen)
          else:
            incoming.remove(clisk)
            break
        except socket.error, e:
          print e
          if e[0] == 10054 or e[0] == 104:
            incoming.remove(clisk)
            continue
          else:
            incoming.remove(clisk)
            servsk.close()
            return
          
        try:
          errCode, response = self.operations.get(msgid, self.defaultOp)(clisk, data)
          json = ""
          if response:
            json = zipfile.zlib.compress(simplejson.dumps(response).encode("utf-8"))
            clisk.send(struct.pack("!hi",errCode,len(json)))
            clisk.send(json)
          else:
            clisk.send(struct.pack("!hi",errCode,0))
            
        except socket.error, e:
          print str(e)
          if e[0] == 10054 or e[0] == 104:
            incoming.remove(clisk)
            clisk = None
            continue
          else:
            incoming.remove(clisk)
            servsk.close()
            raise e
        except Exception, e:
          print e
          servsk.close()
          incoming.remove(clisk)
          continue
          
      
    for cli in incoming:
      cli.close()
      
  def defaultOp(self, clisk, data):
    return (0, "unknown operation")

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
    pos.value += 20000
    self.media_control.set_media_position(pos)
    
    return (1,pos.value)
    
  def rewind(self, clisk, data):
    pos = self.media_control.get_media_position(0,0)
    pos.value -= 20000
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
    self.active = False
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
