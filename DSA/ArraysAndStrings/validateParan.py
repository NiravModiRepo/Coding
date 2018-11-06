# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:44:30 2018

@author: Nirav Modi
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    pStack = []
    
    pDic = {"(":")", "{":"}", "[":"]"}
    
    for i in s:
        if i in pDic:
            pStack.append(pDic[i])
        elif i in pDic.values():
            if len(pStack) < 1:
                return False
            j = pStack.pop()
            if j != i:
                return False
        
    if len(pStack):
        return False
    return True

print(isValid("()"))