# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:49:02 2018

@author: Nirav Modi
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        if (root.left is None) and (root.right is None):
            if sum - root.val:
                return False
            else:
                return True
            
        if self.hasPathSum(root.left, sum - root.val):
            return True
        return self.hasPathSum(root.right, sum - root.val)
    
solution = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)



print(solution.hasPathSum(root, 22))