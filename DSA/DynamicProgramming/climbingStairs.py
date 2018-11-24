# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 23:25:41 2018

@author: Nirav Modi

2-1 Fibonacci Number
"""

def computeFib(n):
    
    if n < 2:
        return n
    return computeFib(n-1) + computeFib(n-2)