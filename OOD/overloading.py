# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:27:54 2018

@author: Nirav Modi
"""

class Square:
    def __init__(self, side):
        self.side = side
        
    def __add__(squareOne, squareTwo):
        return (4 * squareOne.side) + (4 * squareTwo.side)
        
squareOne = Square(5) # 5 * 4 = 20
squareTwo = Square(10) # 10 * 4 = 40

print("Sum of Sides of both squares = ", squareOne + squareTwo)

