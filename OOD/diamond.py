# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:19:46 2018

@author: Nirav Modi
"""

class A:
    def method(self):
        print("This method belongs to class A")
    pass

class B(A):
    def method(self):
        print("This method belongs to class B")
    pass

class C(A):
    def method(self):
        print("This method belongs to class C")
    pass

class D(B, C):
    pass

d = D()
d.method()