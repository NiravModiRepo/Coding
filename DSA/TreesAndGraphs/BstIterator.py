# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:17:07 2018

@author: Nirav Modi

github: https://github.com/NiravModiRepo/Coding/tree/master/DSA

https://leetcode.com/problems/binary-search-tree-iterator/description/
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        #create a stack, at most this will be O(h)
        self.stack = []
        #fill the stack with left nodes from the root
        while(root is not None):
            self.stack.append(root)
            root=root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        #return if stack is full or empty
        if len(self.stack):
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        #pop the next node in the stack
        node = self.stack.pop()
        
        #check the right subtree
        travNode = node.right
        #fill the left nodes of the right subtree
        while(travNode is not None):
            self.stack.append(travNode)
            travNode=travNode.left
            
        #return the value of the node    
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())