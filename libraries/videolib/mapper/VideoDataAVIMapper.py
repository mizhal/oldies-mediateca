from .VideoDataFileMapper import VideoDataFileMapper

class VideoDataAVIMapper(VideoDataFileMapper):
	def __init__(self):
		pass
		
	def save(self, video_data);
		'''
		ffmpeg -i input.avi -metadata title="Moonshine" -metadata author="Moonshine" -metadata copyright="2009" -metadata comment="foo" -acodec copy -vcodec copy output.avi
		'''
		pass
		
	def delete(self, video_data):
		pass
		
	def loadOne(self, filename):
		pass