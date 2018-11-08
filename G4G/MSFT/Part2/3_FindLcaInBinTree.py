# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:55:36 2018

@author: Nirav Modi

Find LCA in a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # if the head is none or if you reached the end of the tree
        if (root is None) or (p is None) or (q is None):
            return None
        
        # if you reached a matching value, return it up
        if (root.val == p.val) or (root.val == q.val):
            return root
        
        #check the left and right subtree ro find a matching node
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # if one value is to the left and one to the right, return current node
        if (left is not None) and (right is not None):
            return root
        
        # if you only found a value on one side, return that node
        if left is None:
            return right
        else:
            return left
            
            
        