import socket
import struct
import simplejson
import zipfile

from exceptions import Exception

## constantes identificadoras de operacion
from op_constants import *

class CannotConnect(Exception):
  def __init__(self, msg):
    self.msg = msg
  def __str__(self):
    return "Cannot Connect: %s"%self.msg

class MediatecaClient:
  def __init__(self, server_host, server_port, 
      max_repeats = 5, timeout = 5):
      
    self.max_repeat = max_repeats
    self.timeout = timeout
    self.server_host = server_host
    self.server_port = server_port
    try:
      self._connect()
    except Exception, e:
      raise CannotConnect(str(e))
    
  def __del__(self):
    self.sk.close()
    
  def _connect(self):
    self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sk.connect((self.server_host, self.server_port))
    self.sk.settimeout(self.timeout)
    
  def _communicate(self, msg, repeats = 0):
    try:
      self.sk.send(msg)
    
      header = self.sk.recv(6)
      if len(header) > 0:
        err_code, length = struct.unpack("!hi", header)
        if length > 0:
        	data = zipfile.zlib.decompress(self.sk.recv(length))
        	return simplejson.loads(data)
      else:
        raise Exception()
    except Exception, e:
      if repeats < self.max_repeat:
        self._connect()
        return self._communicate(msg, repeats+1)
      else:
        raise CannotConnect("max repeats reached (socket lib error: %s)"%str(e))

  def resume(self):
    msg = struct.pack("!hh",3,0)
    return self._communicate(msg)
    
  def pause(self):
    msg = struct.pack("!hh",4,0)
    return self._communicate(msg)
    
  def next(self):
    msg = struct.pack("!hh",1,0)
    return self._communicate(msg)
    
  def prev(self):
    msg = struct.pack("!hh",2,0)
    return self._communicate(msg)
    
  def advance(self):
    msg = struct.pack("!hh",5,0)
    return self._communicate(msg)
    
  def rewind(self):
    msg = struct.pack("!hh",6,0)
    return self._communicate(msg)
    
  def fullscreen(self):
    msg = struct.pack("!hh",8,0)
    return self._communicate(msg)
    
  def jumpTo(self, pos):
    msg = struct.pack("!hhh",7,2,pos)
    return self._communicate(msg)
    
  def playlist(self, start, end):
    msg = struct.pack("!hhii",9,8,start,end)
    return self._communicate(msg)
      
  def shutdown(self):
    msg = struct.pack("!hh",SHUTDOWN,0)
    return self._communicate(msg)
      
  def sort(self):
    msg = struct.pack("!hh",10,0)
    return self._communicate(msg)
  
  def reloadBase(self):
    msg = struct.pack("!hh",15,0)
    return self._communicate(msg)
      
  def playlistLength(self):
    msg = struct.pack("!hh",11,0)
    return self._communicate(msg)
        
  def getPosition(self):
    msg = struct.pack("!hh",13,0)
    return self._communicate(msg)
        
  def setPosition(self, pos):
    msg = struct.pack("!hhi", 14, 4, pos)
    return self._communicate(msg)

  def getStreamLength(self):
    msg = struct.pack("!hh", STREAM_LENGTH, 0)
    return self._communicate(msg)

  def addFromDir(self, dir):
    msg = struct.pack("!hhi", ADD_FROM_DIR, 4+len(dir), len(dir))
    msg += dir.decode('utf8')
    return self._communicate(msg)