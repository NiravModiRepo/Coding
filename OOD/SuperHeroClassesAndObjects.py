# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:12:19 2018

@author: Nirav
"""

"""

"""



class Mutant:
    
    def __init__(self, name):
        self.name = name
        self.codeName = ""
        self.mutation = False
    
    def goneThroughMutation(self):
        s = self.name + " has "
        if self.mutation:
            s += "gone through mutation."
        else:
            s += "not gone through mutation."
            
        print(s)
        
        return
    
    @staticmethod
    def greet():
        print("Greeting")
        

class Human:
    
    def __init__ (self, name):
        self.name = name
        self.codeName = ""
        self.enhanced = False
        
    def isEnhanced(self):
        s = self.name + " is "
        if self.enhanced:
            s+= "enhanced."
        else:
            s+= "not enhanced."
            
        print(s)
        
        return

class Inhuman:
    
    def __init__ (self, name):
        self.name = name
        self.codeName = ""
        self.terrigenesis = False
        
    def goneThroughTerrigenesis(self):
        s = self.name + " has "
        if self.terrigenesis:
            s += "gone through terrigenesis."
        else:
            s += "not gone through terrigenesis."
        
        print(s)
        
        return
    
"""
Illumanati comics

Mr. Fantastic - Reed Richards
Iron Man - Tony Stark
Ant Man - Hank Pym
Hulk - Bruce Banner
Black Panther - T'Challa
Beast - Hank McCoy
Professor X - Charles Xavier

Justin Hammer
Dr. Doom - Victor Van Doom
Green Goblin - Norman Osborn
Doc Ock - Otto Octavius
The Leader - Samuel Sterns

"""    