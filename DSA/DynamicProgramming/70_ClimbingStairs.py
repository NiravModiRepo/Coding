# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:02:33 2018

@author: Nirav Modi

Runtime: O(n)
"""

class Solution:
    
    # Base dictionary for the stairs
    dictStairs = {0:0, 1:1, 2:2, 3:3}
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # If it already is in the dictionary, return it
        if n in self.dictStairs:
            return self.dictStairs[n]
        
        # If the value is not in the dictionary, recurse down and add the entry
        self.dictStairs[n] =  self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # Return the value in the entry
        return self.dictStairs[n]