from sys import argv

from MediatecaClient import MediatecaClient
from uri_filters.youtube import playable_url


c = MediatecaClient("192.168.1.7",16667)
c.playMRL(playable_url(argv[1]))
