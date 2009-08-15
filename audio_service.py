import pygst
pygst.require("0.10")
import gst
from threading import Thread, Lock

from time import sleep

class Playlist:
        class End(Exception):
                pass
                
        class BeforeStart(Exception):
                pass
        
        def __init__(self, files):
                self.files = files
                self.cnt = -1
                
        def next(self):
                self.cnt += 1
                if self.cnt >= len(self.files):
                        self.cnt = 0
                return self.files[self.cnt]
 
        def prev(self):
                self.cnt -= 1
                if self.cnt < 0:
                        raise Playlist.BeforeStart()
                return self.files[self.cnt] 

class AudioService(Thread):
        PLAYING = 0
        STOPPED = 1
        RANDOM = 2
        NOT_RANDOM = 3
        REPEAT_ALL = 4
        REPEAT_ONE = 5
        
        def __init__(self, playlist_provider):
                Thread.__init__(self)
                
                self.playlist = playlist_provider.getPlaylist()
                
                self.executive = gst.element_factory_make("playbin", "player")
                #para que estas conexiones de mensajes funciones debe 
                #haber un mainloop de GLib en el proceso. En ipython
                #debe de haberse iniciado con la opcion -gthread
                bus = self.executive.get_bus() 
                bus.add_signal_watch()
                bus.connect("message", self.on_message)
                
                self.status = AudioService.STOPPED
                
                self.lock = Lock()
                
        def on_message(self, bus, message):
                t = message.type
                if t == gst.MESSAGE_EOS:
                        self.executive.set_state(gst.STATE_READY)
                        self.next()
                elif t == gst.MESSAGE_ERROR:
                        self.executive.set_state(gst.STATE_NULL)
                        err, debug = message.parse_error()
                        print "Error: %s" % err, debug
                
        def play(self):
                if self.status == AudioService.STOPPED:
                        self.next()
                        
        def stop(self):
                self.lock.acquire()
                self.executive.set_state(gst.STATE_NULL)
                self.lock.release()
    
        def next(self):
                self.lock.acquire()
                
                nn = self.playlist.next()
                self.executive.set_state(gst.STATE_NULL)
                self.executive.set_property("uri", nn) 
                
                self.executive.set_state(gst.STATE_PLAYING)
                self.status = AudioService.PLAYING
                
                self.lock.release()

        def prev(self):
                self.lock.acquire()
                
                pv = self.playlist.prev()
                self.executive.set_state(gst.STATE_NULL)
                self.executive.set_property("uri", pv) #NOTE: las uris locales requieren "file://"
                #self.executive.connect(gst.MESSAGE_EOS, self.next)#ENG-POINT: asociar el evento End of Stream a la rutina que pasa a la siguiente cancion
                self.executive.set_state(gst.STATE_PLAYING)
                self.status = AudioService.PLAYING
                
                self.lock.release()

## 
# @note soporta facilmente streaming MMS como el de Onda Cero
class PL:
        def getPlaylist(self):
                return Playlist(["file:///media/archivo_general/Mediateca/Audio/sonidos/atraco.wav", "file:///media/archivo_general/Mediateca/Audio/coleccion/Amy Mcdonald - This Is The Life.mp3","file:///media/archivo_general/Mediateca/Audio/coleccion/01-The Order-Roots of Rebellion.mp3", "mms://a241.l507241193.c5072.e.lm.akamaistream.net/D/241/5072/v0001/reflector:41193"])
                
pl = PL()