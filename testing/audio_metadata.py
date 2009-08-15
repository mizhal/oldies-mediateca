import mediateca.audio_base as AB

def test1():
	meta, fail, ign = AB.load("/media/archivo_general/Mediateca/Audio")
	return (meta, fail, ign)