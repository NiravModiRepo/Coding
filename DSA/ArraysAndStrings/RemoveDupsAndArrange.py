# -*- coding: utf-8 -*-
"""
Remove Dups from a string and arrage its letters in order

@author: Nirav Modi
"""

def removeDupsAndArrange(string):
    
    wordDict = {}
    result = ''
    alphabets='abcdefghijklmnopqrstuvwxyz'
    
    #put words in a dictionary
    for i in range(len(string)):
        if string[i] not in wordDict:
            wordDict[string[i]]=1
            
    #arrage letters
    for i in alphabets:
        if i in wordDict:
            result +=i
            
    return result
    
            


print(removeDupsAndArrange('geeksforgeeks'))
            
        