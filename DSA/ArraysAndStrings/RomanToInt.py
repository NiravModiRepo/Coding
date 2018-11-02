# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:08:24 2018

@author: Nirav Modi

https://leetcode.com/problems/roman-to-integer/description/

convert string from roman numerals to integer

This solution is O(N) time and O(1) space
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dictionary for all possible input characters
        r2i = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        #if the string is empty, return nothing
        if len(s) < 1:
            return ""
        
        if len(s) > 15:
            return
        
        #if the string is single character or already in the dictionary
        if s in r2i:
            return r2i[s]
        
        #return value that keeps incrementing
        retVal = 0
        #flag for skipping a character
        flag = True
        
        for i in range(0,len(s)):
            
            if (flag):
                if (i == (len(s)-1)):
                    retVal += r2i[s[i]]
                    
                elif (s[i] == "I") and (s[i+1] == "V"):
                    retVal += 4
                    flag = False #flag tripped to skip next value
                elif (s[i] == "I") and (s[i+1] == "X"):
                    retVal += 9
                    flag = False
                elif (s[i] == "X") and (s[i+1] == "L"):
                    retVal += 40
                    flag = False
                elif (s[i] == "X") and (s[i+1] == "C"):
                    retVal += 90
                    flag = False
                elif (s[i] == "C") and (s[i+1] == "D"):
                    retVal += 400
                    flag = False
                elif (s[i] == "C") and (s[i+1] == "M"):
                    retVal += 900
                    flag = False
                
                else:
                    retVal += r2i[s[i]]
            else:
                flag = True #reset flag
        
        
        #This part is an optional memoization approach that can be discussed.
        #It would grow the space complexity but eventually be capped at 4000.
        #For this specific problem on leetcode, it is stated that input
        #is guaranteed to be within 1 to 3999.
        #O(4000) -> O(1), so we would still be operating at O(1) space.
        #This would allow repeated input values to respond at O(1) time,
        #instead of O(N) time.
        r2i[s]=retVal
        
        return retVal
            


s = "MMMXLV"
       
sol = Solution()
print(sol.romanToInt(s))