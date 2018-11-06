# -*- coding: utf-8 -*-
"""
Search for Element in a rotated array

[7, 8, 9, 1, 2, 3, 4, 5]

Search for 3
Find it in log n

Find starting point in log n
Find value in log n
O(2log N)->O(log N)

@author: Nirav Modi

LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""
       
def findRotPoint(n, start, end):
    
    if end < start:
        return -1
    
    if start == end:
        return start
    
    if abs(start-end) == 1:
        if min(n[start], n[end]) == n[start]:
            return start
        else:
            return end
    
    mid = (start+end)//2
       
    if n[mid] > n[start]:
        return findRotPoint(n,mid, end)
    else:# n[mid] < n[start]:
        return findRotPoint(n, start, mid)
    
def binSearch(n, k, start, end):
    
    
    if end < start:
        return -1
   
    mid = (start+end)//2
    
    if n[mid] == k:
        return mid
    
    if n[mid] > k:
        return binSearch(n, k, start, mid-1)
    else:
        return binSearch(n, k, mid+1, end)

def findValueInRotatedArray(n, k):
    
    if len(n) == 0:
        return -1
    
	#Find the rotational point, it takes LogN time
    rotPoint = findRotPoint(n, 0, len(n)-1)
    
	#Search either left or right of rotational point, takes LogN time
    if (k >= n[rotPoint]) and (k <= n[len(n)-1]):
        return binSearch(n, k, rotPoint, len(n)-1)
    else:
        return binSearch(n, k, 0, rotPoint)


# Tests
print(findValueInRotatedArray([7,8,9,1,2,3,4,5], 3))
#answer should be 5

