from os import listdir, walk
from os.path import join, exists, isdir

extensions = [".wmv", ".avi", ".ogm", ".mkv"]

class Playlist:
        def __init__(self, files):
                self.files = files
                self.cursor = 0

        def next(self):
                self.cursor += 1
                if self.cursor < len(self.files):
                        return self.files[self.cursor-1]
                else:
                        return None
        
        def prev(self):
                self.cursor -= 1
                if self.cursor < len(self.files):
                        return self.files[self.cursor]
                else:
                        return None
                
        def get(self, pos):
                self.cursor = pos
                return self.files[self.cursor]
                
        def ls(self):
                return [file.split("/")[-1] for file in self.files]

        def sort(self):
                self.files.sort()
                
        def count(self):
                return len(self.files)

	def addFromDir(self, dir):
		for root, dirs, files in walk(dir):
			for fname in files:
				if reduce(lambda x,y: x or y, map(lambda x: fname.endswith(x), extensions)):
					self.files.append(join(root, fname))

class VideoBase:
        
        def __init__(self, *dirs):
                self.dir = dirs
                
                self.files = []
                self.metadata = []
                                                        
        def _load(self, dirs):
                for dir in dirs:
                    self.files = []
                    for root, dirs, files in walk(dir):
                        for fname in files:
                            if reduce(lambda x,y: x or y, map(lambda x: fname.endswith(x), extensions)):
                                self.files.append(join(root, fname))
                
        def getPlaylistAll(self):
                self._load(self.dir)
                return Playlist(self.files)
                
def get_meta(fname):
        from hachoir_core.error import HachoirError
        from hachoir_core.cmd_line import unicodeFilename
        from hachoir_parser import createParser
        from hachoir_core.tools import makePrintable
        from hachoir_metadata import extractMetadata
        from hachoir_core.i18n import getTerminalCharset
        
        
        filename, realname = unicodeFilename(fname), fname
        parser = createParser(filename, realname)
        if not parser:
            print >>stderr, "Unable to parse file"
            exit(1)
        try:
            metadata = extractMetadata(parser)
        except HachoirError, err:
            print "Metadata extraction error: %s" % unicode(err)
            metadata = None
        if not metadata:
            print "Unable to extract metadata for %s"%fname
        else:
                return metadata
