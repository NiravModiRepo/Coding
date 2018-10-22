# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:22:41 2018

The Four Pillars of OOP in Python 3 for Beginners
Created by Febin George
EXERCISE - ATTRIBUTES AND METHODS
Write an object oriented program to create a precious stone. 
Not more than 5 precious stones can be held in possession at a given point of time. 
If there are more than 5 precious stones, delete the first stone and store the new one.


@author: Nirav Modi
"""

#Define Stone Class
class stone:
    #Initialize number of stones to 0
    numOfStones = 0
    #Initialize Stone Queue
    stoneCollection = []
    
    def __init__(self, name):
        
        self.name = name
        
        stone.numOfStones +=1
        
        if stone.numOfStones > 5:
            stone.stoneCollection.pop(0)
        
        stone.stoneCollection.append(self)
    
    #Static method to display every stone
    @staticmethod
    def displayStones():
        for i in stone.stoneCollection:
            print(i.name)



        