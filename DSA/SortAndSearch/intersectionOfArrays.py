# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:50:16 2018

@author: Nirav Modi

https://leetcode.com/problems/intersection-of-two-arrays/
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        #return list(set(nums1) & set(nums2))
        
        minLen = min(len(nums1), len(nums2))
        
        if (minLen < 1):
            return []
        
        nums1.sort()
        nums2.sort()
        
        resultArray = []
        
        i = 0
        j = 0
        
        prev = -float('inf')
        
        while ((i < len(nums1)) and (j < len(nums2))):
            
            if (nums1[i] == nums2[j]) and (nums1[i] != prev):
                prev = nums1[i]
                resultArray.append(prev)
                i+=1
                j+=1
            
            elif nums1[i] > nums2[j]:
                j+=1
                
            else:
                i+=1
        
        return resultArray
            
            
    
    
solution = Solution()

print(solution.intersection([4,9,5], [9,4,9,8,4]))            
        
        
        