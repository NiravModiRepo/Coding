# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 23:25:41 2018

@author: Nirav Modi

2-1 Fibonacci Number


First one takes a long time

"""

def naiveFib(n):
    
    if n < 2:
        return n
    return naiveFib(n-1) + naiveFib(n-2)

def listFib(n):
    
    dictFib = {}
    dictFib[0] = 0
    dictFib[1] = 1
    
    if n in dictFib:
        return dictFib[n]
    
    for i in range(2,n+1):
        dictFib[i] = dictFib[i-1] + dictFib[i-2]
    
    return dictFib[n]