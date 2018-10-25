# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:36:52 2018

@author: Nirav Modi
"""

class MusicalInstruments:
    numberOfMajorKeys = 12
    
class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"
    
class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {} strings. It is made of {} and it can play {} keys".format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))
        
guitar = Guitar()