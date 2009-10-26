from exceptions import Exception

import bluetooth as bt
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
    
  def setOp(self, key, handler):
    self.operations[key] = handler
    
  def run(self):
    servsk = bt.BluetoothSocket( bt.RFCOMM )
    
    #servsk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servsk.bind(("", self.port))
    servsk.listen(10)
    
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    bt.advertise_service( servsk, "RPC BT Server",
                   service_id = uuid,
                   service_classes = [ uuid, bt.SERIAL_PORT_CLASS ],
                   profiles = [ bt.SERIAL_PORT_PROFILE ], 
                   # protocols = [ OBEX_UUID ] 
                    )
    
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
        except Exception, e:
          print str(e)
           
          incoming.remove(clisk)
          continue
          
        try:
          errCode, response = self.operations.get(msgid, self.defaultOp)(clisk, data)
          json = ""
          if response:
            json = zipfile.zlib.compress(simplejson.dumps(response).encode("utf-8"))
            clisk.send(struct.pack("!hi",errCode,len(json)))
            clisk.send(json)
          else:
            clisk.send(struct.pack("!hi",errCode,0))
            
        except Exception, e:
          ## @todo GESTIONAR LAS EXCEPCIONES DE DESCONEXION DEL PAR FRENTE A OTRAS
          print str(e)
           
          incoming.remove(clisk)
          continue
      
    for cli in incoming:
      cli.close()
      
  def defaultOp(self, clisk, data):
    return (0, "unknown operation")
    
  def security(self, clisk, address):
    return True
