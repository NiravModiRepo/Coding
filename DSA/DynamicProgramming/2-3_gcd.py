# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:47:32 2018

@author: Nirav Modi

Greatest Common Divisor
"""

def naiveGcd(a, b):
    
    best = 1
    
    for d in range(1, a+b+1):
        
        if (((d/a) % 1) == 0) and (((d/b) % 1) == 0):
            best = d
        
    return best

print(naiveGcd(1344,217))




def euclidGcd(a, b):
    if b == 0:
        return a
    
    print("a = ", a, "b = ", b)
    return euclidGcd(b, a%b)


#print(euclidGcd(1344,217))