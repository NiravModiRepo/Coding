# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:17:08 2018

@author: Nirav Modi


Fibonacci
"""

class Solution:
    
    fibDict = {0:0, 1:1}
    
    def fib(self, n):
        
        if n in self.fibDict:
            return self.fibDict[n]
        
        self.fibDict[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.fibDict[n]


solution = Solution()
print(solution.fib(14))