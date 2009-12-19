import pygst
pygst.require("0.10")
import gst

class GStreamerAudioEngine:
	def __init__(self):
		self.audio_control = gst.element_factory_make("playbin", "player")
		self.playlist = None
		
	def connectPlaylistEngine(self, playlist):
		self.playlist = playlist
		
	def next(self):
		stream = self.playlist.next()
		self.audio_control.set_property("uri", stream.uri)
		self.audio_control.set_state(gst.STATE_PLAYING)
		return stream
		
	def prev(self):
		stream = self.playlist.prev()
		self.audio_control.set_property("uri", stream.uri)
		self.audio_control.set_state(gst.STATE_PLAYING)
		return stream

  def stop(self, clisk, data):
    return (1, None)

	def pause(self):
		pass
		
	def play(self):
		pass

	def advance(self, clisk, data):
		return (1,pos.value)

  def rewind(self, clisk, data):
    return (1,pos.value)

	def reload(self, clisk, data):
		pass

  def fullscreen(self, clisk, data):
    return (1,None)
    
  def getPlaylist(self, clisk, data):
    start, end = struct.unpack("!ii",data)
    return (1, self.playlist.ls()[start: end])
    
  def sort(self, clisk, data):
    self.playlist.sort()
    return (1, None)
    
  def length(self, clisk, data):
    return (1, self.playlist.count())
    
  def getPos(self, clisk, data):
    pos = self.media_control.get_media_position(0,0)
    return (1, pos.value)
        
  def setPos(self, clisk, data):
    curr = self.media_control.get_media_position(0,0).value
    pos = struct.unpack("!i",data)[0];
    self.media_control.set_media_position(pos - curr)
    return (1, None)    

  def addFromDir(self, clisk, data):
    len = struct.unpack("!i",data[:sizeof(c_int)])[0]
    dir = data[sizeof(c_int):len+sizeof(c_int)].encode("utf-8")
    if exists(dir):
      self.playlist.addFromDir(dir)
      return (1, None)
    else:
      return (0, "Directory not found")
  
  def streamLength(self, clisk, data):
    return (1, media_length)
	