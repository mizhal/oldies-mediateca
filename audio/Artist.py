'''
Created on 15/08/2009

@author: mizhal
'''

from data_sessions import getSession

class Artist(object):
    '''
    classdocs
    '''
    name = "desconocido"
    web = None
    rss = None
    info_codex = None

    def __init__(selfparams):
        '''
        Constructor
        '''
        
    @staticmethod
    def getInstance(self, name):
        return Artist.all_instances.get(name, Artist.Unknown)
        