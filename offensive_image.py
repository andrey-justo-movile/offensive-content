'''
Created on Dec 7, 2016

@author: andrey.justo

Usage of https://github.com/hhatto/nude.py

'''

import nude
from nude import Nude

class OffensiveImage():

    def __init__(self, path):
        self.nude_image = Nude(path)
        
    def is_nude(self):
        return self.nude_image.parse().result()


#tests made a poor performance and a lot of false positive
print(OffensiveImage('./images/nude-1.jpeg').is_nude())
