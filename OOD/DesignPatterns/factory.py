# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:28:41 2018

@author: Nirav Modi

https://www.youtube.com/watch?v=flOXIdWUpmU
Factory Method
"""

#A design patter which lets a function which class to create

BaseClass = type("BaseClass", (object,),{})
C1 = type("C1", (BaseClass,), {"x":1})
C2 = type("C2", (BaseClass,), {"x":30})

def MyFactory(myBool):
    return C1() if myBool else C2()

m = MyFactory(True)
v = MyFactory(False)

print(m.x, v.x)