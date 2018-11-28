# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:20:20 2018

@author: Nirav Modi

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Brute Force would be O(n^n) time and O(n) space.
    This would mean you recursively go through each combination
    Depth of recursion would be O(n)
    This would take way too long
    
The optimized solution is O(n) space.
It is explained in the code below.


"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Here are net profit and running profit values initialized
        runningProfit = 0
        netProfit = runningProfit
        
        # If it is an invalid input, return netProfit = 0
        if len(prices) < 2:
            return netProfit
        
        # Walk through the input starting with the second entry
        for i in range(1,len(prices)):
            
            # No need to call them pre/current but did it to make code look readable
            pre = prices[i-1]
            current = prices[i]
            
            # If there is not a loss, keep accumulating profits
            # Could have made this if statement if (current - pre) > 0
            if pre < current:
                runningProfit += current - pre
            # If there is a loss, sell right away
            # Add the current profits to netProfit and reset current profits
            else:
                netProfit += runningProfit
                runningProfit = 0
            
        # Add current profits to net profit, in case there were any at the end
        netProfit += runningProfit
        
        # Return net profit
        return netProfit




solution = Solution()


print(solution.maxProfit([7,1,5,3,6,4]))

print(solution.maxProfit([1,2,3,4,5]))

print(solution.maxProfit([7,6,4,3,1]))