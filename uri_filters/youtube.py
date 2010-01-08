# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
##@source: http://geniusofevil.wordpress.com/2009/04/30/howto-get-direct-youtube-video-flv-url/

import httplib,urllib
__author__ = 'Jarosław Przygódzki'
__copyright__ = 'Copyright (c) 2009 Jarosław Przygódzki'
__date__ = '30.04.2009'
__license__ = 'GPL'
__version__ = '0.1.1'

def GetYoutubeVideoInfo(videoID,eurl=None):
	'''
	Return direct URL to video and dictionary containing additional info
	>> url,info = GetYoutubeVideoInfo("tmFbteHdiSw")
	>>
	'''
	if not eurl:
		params = urllib.urlencode({'video_id':videoID})
	else :
		params = urllib.urlencode({'video_id':videoID, 'eurl':eurl})
	conn = httplib.HTTPConnection("www.youtube.com")
	conn.request("GET","/get_video_info?&%s"%params)
	response = conn.getresponse()
	data = response.read()
	video_info = dict((k,urllib.unquote_plus(v)) for k,v in (nvp.split('=') for nvp in data.split('&')))
	conn.request('GET','/get_video?video_id=%s&t=%s' % ( video_info['video_id'],video_info['token']))
	response = conn.getresponse()
	direct_url = response.getheader('location')
	return direct_url,video_info


def playable_url(youtube_url):
	for pair in urllib.splitquery(youtube_url)[1].split("&"):
		k, v = pair.split("=")
		if k == 'v':
			return GetYoutubeVideoInfo(v)[0]