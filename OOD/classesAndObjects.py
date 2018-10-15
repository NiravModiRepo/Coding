# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:22:41 2018

@author: 22848
"""

class stone:
    numOfStones = 0
    stoneCollection = []
    
    def __init__(self, name):
        
        self.name = name
        
        stone.numOfStones +=1
        
        if stone.numOfStones > 5:
            stone.stoneCollection.pop(0)
        
        stone.stoneCollection.append(self)
    
    @staticmethod
    def displayStones():
        for i in stone.stoneCollection:
            print(i.name)



        