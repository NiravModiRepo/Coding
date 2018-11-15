# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:27:23 2018

@author: Nirav Modi

https://leetcode.com/problems/maximum-product-subarray/description/
"""

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 1:
            return 0
        
        if len(nums) < 2:
            return nums[0]
        
        result = nums[0]
        maxProd = nums[0]
        minProd = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] < 0:
                temp = maxProd
                maxProd = minProd
                minProd = temp
            
            maxProd = max(nums[i], maxProd * nums[i])
            minProd = min(nums[i], minProd * nums[i])
            result = max(result, maxProd)
            
            
        return result
        
        
solution = Solution()


array = [0,2]        
print(solution.maxProduct(array))