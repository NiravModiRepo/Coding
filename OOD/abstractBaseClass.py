# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:40:17 2018

@author: Nirav Modi
"""
from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0
    

class Square(Shape):
    side = 4
    def area(self):
        print ("Area of Square: ", self.side * self.side)
        
class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print ("Area of Rectangle: ", self.width * self.length)


square = Square()
rectangle = Rectangle()

square.area()
rectangle.area()

#shape = Shape()