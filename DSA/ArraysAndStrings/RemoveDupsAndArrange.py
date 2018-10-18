# -*- coding: utf-8 -*-
"""
Remove Dups from a string and arrage its letters in order

@author: Nirav Modi
"""

def removeDupsAndArrange(string):
    
    wordDict = {}
    
    for i in range(len(string)):
        if string[i] not in wordDict:
            
            
        