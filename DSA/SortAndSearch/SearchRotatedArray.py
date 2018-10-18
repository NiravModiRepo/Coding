# -*- coding: utf-8 -*-
"""
Search for Element in a rotated array

[7, 8, 9, 1, 2, 3, 4, 5]

Search for 3
Find it in log n

Find starting point in log n
Find value in log n
O(2log N)->O(log N)

@author: 22848
"""
       

def findValueInRotatedArray(n, k):
    
    if len(n) == 0:
        return -1
    
    left = 0
    right = len(n)-1



# Tests
findValueInRotatedArray([7,8,9,1,2,3,4,5], 3)
#answer should be 5

