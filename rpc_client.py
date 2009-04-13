import socket
import struct
import simplejson

class MediatecaClient:
  def __init__(self, server_host, server_port):
    self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sk.connect((server_host, server_port))
    
  def __del__(self):
    self.sk.close()
    
  def resume(self):
    msg = struct.pack("!hh",3,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
    
  def pause(self):
    msg = struct.pack("!hh",4,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
    
  def next(self):
    msg = struct.pack("!hh",1,0)
    self.sk.send(msg)

    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
      return simplejson.loads(data)
    
  def prev(self):
    msg = struct.pack("!hh",2,0)
    self.sk.send(msg)
        
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
      return simplejson.loads(data)
    
  def advance(self):
    msg = struct.pack("!hh",5,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
    
  def rewind(self):
    msg = struct.pack("!hh",6,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
    
  def fullscreen(self):
    msg = struct.pack("!hh",8,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
    
  def jumpTo(self, pos):
    msg = struct.pack("!hhh",7,2,pos)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
      return simplejson.loads(data)
    
  def playlist(self, start, end):
    msg = struct.pack("!hhii",9,8,start,end)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    if len(header) > 0:
      err_code, length = struct.unpack("!hi", header)
      if length > 0:
        data = self.sk.recv(length)
        return simplejson.loads(data)
      
  def stop(self):
    msg = struct.pack("!hh",12,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
      
  def sort(self):
    msg = struct.pack("!hh",10,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)
      
  def playlistLength(self):
    msg = struct.pack("!hh",11,0)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    if len(header) > 0:
      err_code, length = struct.unpack("!hi", header)
      if length > 0:
        data = self.sk.recv(length)
        return simplejson.loads(data)
        
  def getPosition(self):
     msg = struct.pack("!hh",13,0)
     self.sk.send(msg)
    
     header = self.sk.recv(6)
     if len(header) > 0:
       err_code, length = struct.unpack("!hi", header)
       if length > 0:
         data = self.sk.recv(length)
         return simplejson.loads(data)
        
  def setPosition(self, pos):
    msg = struct.pack("!hhi", 14, 4, pos)
    self.sk.send(msg)
    
    header = self.sk.recv(6)
    err_code, length = struct.unpack("!hi", header)
    if length > 0:
      data = self.sk.recv(length)