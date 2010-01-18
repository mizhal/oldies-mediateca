#! /usr/bin/python
from MediatecaServer import MediatecaServer

## LOG  
import logging
LOG_FILENAME = '/tmp/mediateca-watchdog.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

logging.info('Iniciando el sistema mediateca')

## Redireccion de la salida de error, para capturar 
## errores en los hilos
class LOG:
    def __init__(self):
        self.log = logging.getLogger()
    def write(self, text):
        self.log.error(text)
        
import sys

sys.stderr = LOG()

try:
    server = MediatecaServer()
except:
   logging.exception('Error en el subsistema principal')
    
