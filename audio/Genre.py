'''
Created on 15/08/2009

@author: mizhal
'''

from data_sessions import getSession

class Genre(object):
    '''
    classdocs
    '''
    name = "desconocido"
    description = "" 

    def __init__(self, name, description = ""):
        '''
        Constructor
        '''
        
    def __new__(cls, *attrs):
        session = getSession()
        return session.query(Genre)
        
    @staticmethod
    def getGenre(name):
        return Genre.all_genres.get(name, Genre(name))
        
        