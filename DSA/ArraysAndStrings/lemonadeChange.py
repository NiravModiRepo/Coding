# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:08:10 2018

@author: Nirav Modi

https://leetcode.com/problems/lemonade-change/

This takes O(n) time

"""

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if len(bills) < 1:
            return True
        
        # amount of 5's and 10's in the change drawer
        five = 0
        ten = 0
        
        # walk through each transaction
        for i in bills:
            
            # perfect change, add it to the change drawer
            if i == 5:
                five +=1
            
            # imperfect change, return a five or error
            elif i == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
                
            # customer gives $20, return three $5's or a $10 and a $5
            else:
                if (five > 0) and (ten > 0):
                    five-=1
                    ten-=1
                elif five > 3:
                    five-=3
                else:
                    return False                  
                    
        
        return True
        
solution = Solution()
arr = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]

print(solution.lemonadeChange(arr))    