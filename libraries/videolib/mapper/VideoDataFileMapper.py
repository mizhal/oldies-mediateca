from ..model.VideoData import VideoData

class VideoDataFileMapper:
	def __init__(self):
		pass
		
	def save(self, video_data);
		pass
		
	def delete(self, video_data):
		pass
		
	def loadOne(self, filename):
		pass
		
	def loadMany(self, files):
		results = []
		for file in files:
			results.append(self.loadOne(file))
		return results