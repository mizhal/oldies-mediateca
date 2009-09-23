import socket
import struct
import simplejson
from threading import Thread
from select import select

from ctypes import *

import zipfile

class RPCServer(Thread):
  
  def __init__(self, port = 16667):
    self.port = port
    self.active = True
    
    self.operations = {}
    
    Thread.__init__(self)
    
  def setOperation(self, key, handler):
    self.operations[key] = handler
    
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
    
  def security(self, clisk, address):
    return True
