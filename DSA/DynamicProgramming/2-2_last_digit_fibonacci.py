# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:15:55 2018

@author: Nirav Modi

2-2
"""

def computeFib2(n):
    
    dictFib = {}
    dictFib[0] = 0
    dictFib[1] = 1
    
    if n in dictFib:
        return dictFib[n]
    
    for i in range(2,n+1):
        dictFib[i] = dictFib[i-1] + dictFib[i-2]
    
    return dictFib[n] % 10

