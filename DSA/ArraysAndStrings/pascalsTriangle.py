# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:25:06 2018

@author: Nirav Modi

https://leetcode.com/problems/pascals-triangle/


Brute Force method 
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # empty output array
        output = []
        
        #if the input is 0, return empty array
        if numRows == 0:
            return output
        
        # initialize the first layer of pascals triangle
        output.append([1])
        
        # running array to append to output array
        running = []
        
        # go from first level to last level
        for i in range (1,numRows):
        
            # reset running array
            running = [1]
            
            # create the running array and go to the second to the last value of the prior level
            for j in range(0,len(output[i-1])-1):
                # enter the addition of the prior values
                running.append(output[i-1][j] + output[i-1][j+1])

            # enter last value into running array
            running.append(1)
            
            # enter running array into the output value
            output.append(running)
        
        
        return output
    

solution = Solution()
print(solution.generate(5))    