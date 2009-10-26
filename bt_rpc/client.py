import socket
import struct
import simplejson

from exceptions import Exception

class CannotConnect(Exception):
  def __init__(self, msg):
    self.msg = msg
  def __str__(self):
    return "Cannot Connect: %s"%self.msg

class RPCClient:
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
          data = self.sk.recv(length)
          return simplejson.loads(data)
      else:
        raise Exception()
    except Exception, e:
      if repeats < self.max_repeat:
        self._connect()
        return self._communicate(msg, repeats+1)
      else:
        raise CannotConnect("max repeats reached (socket lib error: %s)"%str(e))

  def example(self):
    msg = struct.pack("!hh",3,0)
    return self._communicate(msg)