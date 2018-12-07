# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:18:39 2018

@author: Nirav Modi

https://leetcode.com/problems/copy-list-with-random-pointer/
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if head is None:
            return None

        runner = head
        
        while(runner is not None):
            
            copyRunner = RandomListNode(runner.label)
            copyRunner.next = runner.next
            runner.next = copyRunner
            
            runner = runner.next.next
            
            
        runner = head
        
        while (runner is not None):
            
            if (runner.random is not None):
                runner.next.random = runner.random.next
            else:
                runner.next.random = None
            
            runner = runner.next.next

        copyHead = head.next     
        runner = head
        runnerCopy = copyHead
        
        while(runner is not None):
            runner.next = runner.next.next
            
            if runnerCopy.next is not None:
                runnerCopy.next = runnerCopy.next.next
            else:
                runnerCopy.next = None
                
            runner = runner.next
            runnerCopy = runnerCopy.next
        
        return copyHead
    
    


one = RandomListNode(1)
two = RandomListNode(2)
three = RandomListNode(3)
four = RandomListNode(4)

one.next = two
two.next = three
three.next = four

one.random = three
two.random = one
three.random = three
four.random = two


solution = Solution()
copyOne = solution.copyRandomList(one)

runner = copyOne

while(runner is not None):
    
    print(runner.label)
    runner = runner.next