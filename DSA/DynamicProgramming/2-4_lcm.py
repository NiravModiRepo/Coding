# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:07:53 2018

@author: Nirav Modi

Least Common Multiple
"""

def naiveLcm(a,b):
    
    c = max(a,b)
    d = a*b
    
    for i in range(c, d):
        
        if ((i%a) == 0) and ((i%b) == 0):
            return i
    
    return d


print(naiveLcm(6,8))

def euclidLcm(a,b):
    
    if b == 0:
        return a
    
    
    