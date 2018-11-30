# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:43:30 2018

@author: Nirav Modi

https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        This solution will take O(n) time and O(n) space
        Basically finding the max element and returning it.
        
        """
        n = len(nums)/2
        
        directoryOfNums = {}

        for i in nums:
            
            if i in directoryOfNums:
                directoryOfNums[i]+=1
            else:
                directoryOfNums[i]=1
                
            if (directoryOfNums[i] >= (n)):
                return i

class Solution2:
    """
    This solution thats O(nlogn) time and O(n) space
    After the array is sorted, just take the middle element
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        return nums[len(nums)//2]
        
        

solution = Solution()

print(solution.majorityElement([1]))