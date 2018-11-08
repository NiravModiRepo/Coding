# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:56:27 2018

@author: Nirav Modi

Binary Tree Height Balanced

Time: O(n)
Space: O(h) height

https://leetcode.com/problems/balanced-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if it's a null tree, its balanced
        if root is None:
            return True
        
        # check if the return value is -1
        if self.helperIsBalanced(root, 0) == -1:
            return False
        else:
            return True
    
    def helperIsBalanced(self, node, depth):
        
        # reached the end of the tree, do not increment depth
        if node is None:
            return depth
        
        # current node is valid, increment depth and traverse down
        left = self.helperIsBalanced(node.left, depth+1)
        
        # if left subtree returns an error, return error up
        if left == -1:
            return -1
        
        # current node is valid, increment depth and traverse down
        right = self.helperIsBalanced(node.right, depth+1)
        
        # if right subtree returns an error, return error up
        if right == -1:
            return -1
        
        # check if the subtree values have depth more than 1, return error
        if abs(left-right) > 1:
            return -1
        else:
            # return the max depth in this subtree
            return max(left, right)