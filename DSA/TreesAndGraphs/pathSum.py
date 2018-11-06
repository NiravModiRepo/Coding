# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def hasPathSumHelper(self, node, querySum, currentSum):
        
        if node is None:
            return False
        
        if (node.left is None) and (node.right is None):
            if querySum == (currentSum +node.val):
                return True
            else:
                return False
            
        return self.hasPathSumHelper(node.left, querySum, currentSum + node.val) or self.hasPathSumHelper(node.right, querySum, currentSum + node.val)
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        return self.hasPathSumHelper(root, sum, 0)