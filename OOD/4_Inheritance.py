# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:46:56 2018

The Four Pillars of OOP in Python 3 for Beginners
Created by Febin George
EXERCISE - INHERITANCE
Write an object oriented program that performs the following tasks:
1. Create a class called Chair from the base class Furniture
2. Teakwood should be the type of furniture that is used by all furnitures by default
3. The user can be given an option to change the type of wood used for chair if he wishes to
4. The number of legs of a chair should be a property that should not be altered outside the class

@author: Nirav Modi
"""

class Furniture():
    def __init__(self):
        self._typeOfFurniture = "Teakwood"


class Chair(Furniture):
    __numberOfLegs = 4
    
    def changeWood(self, newType):
        self.typeOfFurniture = newType
        

chair = Chair()

chair.__numberOfLegs = 2

print(chair.__numberOfLegs)
        