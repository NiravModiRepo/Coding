# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:21:43 2018

@author: Nirav Modi

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

This is a backtracking problem where you go through every combination

for example input = "23"

                    Input
                    /|\
                   / | \
                  /  |  \
                 /   |   \
                /    |    \
               /     |     \
              a      b      c
             /|\    /|\    /|\
            d e f  d e f  d e f

RunTime: O(4^n), because every branch can have at max 4 more branches
         where n is the number of letters in the entry

Space: Space would be O(n) without counting the resulting output array.
       The Stack will be O(n) height where n is the length of input

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution:
    
    phoneDict = {}
    phoneDict["2"] = "abc"
    phoneDict["3"] = "def"
    phoneDict["4"] = "ghi"
    phoneDict["5"] = "jkl"
    phoneDict["6"] = "mno"
    phoneDict["7"] = "pqrs"
    phoneDict["8"] = "tuv"
    phoneDict["9"] = "wxyz"
    
    results = []
    
    digits = ""
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # If the input is empty, return empty array
        if len(digits) < 1:
            return []

        # Reset results array and input
        self.results = []
        self.digits = digits
        
        # Recursive call with empty result and first index
        self.letterCombinationsHelper(0, "")
        
        # Return results
        return self.results
    
    def letterCombinationsHelper(self, i, result):
        
        # End of one result, append to results and return, deltes the space on the stack
        if i == len(self.digits):
            self.results.append(result)
            return
        
        # For loop through every letter at the character
        for c in self.phoneDict[self.digits[i]]:
            self.letterCombinationsHelper(i+1, result + c)
            

solution = Solution()            
print(solution.letterCombinations("2"))        
              
        
        
        
        
        
        
        
        