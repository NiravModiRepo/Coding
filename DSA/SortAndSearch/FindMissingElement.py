# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:57:16 2018

@author: Nirav Modi

Given an unsorted array of size 'n' such that only one element occurs twice.
All the elements are from 1 to n. Find the missing element

https://leetcode.com/problems/single-number/description/
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        retVal = 0
        for i in nums:
            retVal ^= i
            
        return retVal