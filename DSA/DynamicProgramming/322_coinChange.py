# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:04:01 2018

@author: Nirav Modi

Coin Change Problem

https://leetcode.com/problems/coin-change/

"""

class Solution:

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if (amount < 1) or (len(coins) < 1):
            return 0
        
        change = [amount+1]*(amount+1)
        change[0] = 0

        for i in range(1, amount+1,1):
            
            for j in range(0, len(coins),1):
                
                if coins[j] <= i:
                    change[i] = min(change[i], change[i-coins[j]] + 1)
                    
        
        if change[amount] > amount:
            return -1
        else:
            return change[amount]      


solution = Solution()

#print(solution.coinChange([1,2,5], 11))
print(solution.coinChange([1,3, 4], 950))


