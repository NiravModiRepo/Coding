# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:09:08 2018

@author: Nirav Modi

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

This is an O(n) solution
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
		# If the array is one or less values, then there is no profit
        if len(prices) < 2:
            return 0
        
		# Initialize profit at zero and minimum value at first value
        profit = 0
        minVal = prices[0]
        
		# Go through each value
        for i in range(len(prices)):

			# if the current price is less than minimum value, reset minimum value
            if prices[i] < minVal:
                minVal = prices[i]
			# if the profit is higher than the max profit, reset max profit	
            elif (prices[i] - minVal) > profit:
                profit = prices[i] - minVal
        
        
        return profit
                
    
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
