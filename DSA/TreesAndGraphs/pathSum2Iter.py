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
        
    def hasPathSum(self, root, querySum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        stack = [(root, 0)]
        
        while (len(stack)):
            
            node, val = stack.pop()
            
            currentSum = val + node.val
            
            if (node.left is None) and (node.right is None):
                if currentSum == querySum:
                    return True
                
            if node.right is not None:
                stack.append((node.right, currentSum))
                
            if node.left is not None:
                stack.append((node.left, currentSum))
                
                
        return False
        
    
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