from os import listdir, walk
from os.path import exists, join, isdir

import mutagen
import tagpy

import re

from exceptions import Exception

## @extension-point estan los nombres de las claves para OGG, MP3 y WMA
metakeys = {
"title":['TIT2', 'title', 'Title'],
"album":['TALB', 'WM/AlbumTitle', 'album'],
"artist":['TPE1',"Author","artist"],
"genre":['TCON',u'WM/Genre',"genre"]
}

fileNameRE = re.compile(r"^.*?([^/\\]+?)[.][^./\\]+$")

class Fail(Exception):
	def __init__(self, str):
		self.str = str
	
class Ignored(Exception):
	pass
	
def extract_tagpy(fname):
	tags = tagpy.FileRef(fname).tag()
	return {
			"title": tags.title,
			"album": tags.album,
			"artist": tags.artist,
			"genre": tags.genre,
			"track": tags.track,
			"year": tags.year
			}

def extract_mutagen(fname):
	md = {}
	try:
		f = mutagen.File(fname)
	except Exception, e:
		print "fallo %s"%fname, e
		raise Fail(e)
		
	if f is None:
		print "ignorado %s"%fname
		raise Ignored()
	for mk, options in metakeys.iteritems():
		for k in options:
			q = f.get(k, None)
			if q:
				if isinstance(q, list):
					md[mk] = [str(i) for i in q]
				elif q.__dict__.has_key("text"):
					md[mk] = [str(i) for i in q.text]
				else:
					md[mk] = q
				continue
	q = md.get("title",None)
	if not q:
		z = fileNameRE.match(fname)
		if z:
			md["title"] = z.groups()[0]
		else:
			md["title"] = fname
			
	return md
	
extensions = [".wma",".mp3",".ogg"]
	
def load(dir):
	''' carga bruta de metadatos de medios 
	de audio en un directorio '''
	metadata = {}
	failed = {}
	ignored = []

	for root, dirs, files in walk(dir):
		for fname in files:
			any = True
			for ext in extensions:
				if fname.endswith(ext):
					any = False
					try:
						metadata[join(root, fname)] = extract_tagpy(join(root, fname))
					except Exception, e:
						try:
							metadata[join(root, fname)] = extract_mutagen(join(root, fname))
						except:
							failed[join(root, fname)] = str(e)
						
					break

			if any:
				ignored.append(join(root, fname))
						
	return (metadata, failed, ignored)
	