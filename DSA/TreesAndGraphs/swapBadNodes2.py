# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 22:26:46 2018

@author: Nirav Modi

https://leetcode.com/problems/recover-binary-search-tree/description/

Morris Traversal
"""

#Tree node initialization
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
#Print nodes in order        
def printInOrder(node, array):
    
    if node is None:
        return
    
    printInOrder(node.left, array)
    
    array.append(node.val)
    
    printInOrder(node.right, array)  

    return array  

class Solution:
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        current = root
        while (current is not None):
            if current.left is None: 
                print(current.val) 
                current = current.right 
            else: 
                # Find the inorder predecessor of current 
                pre = current.left 
                while(pre.right is not None and pre.right != current): 
                    pre = pre.right 
       
                # Make current as right child of its inorder predecessor 
                if(pre.right is None): 
                    pre.right = current 
                    current = current.left 
                      
                # Revert the changes made in if part to restore the  
                # original tree i.e., fix the right child of predecssor 
                else: 
                    pre.right = None
                    print(current.val)
                    current = current.right 
        
        
#Problem from Video    
root1 = TreeNode(7)
root1.left = TreeNode(5)
root1.right = TreeNode(4)
root1.left.right = TreeNode(6)
root1.left.left = TreeNode(8)

#Print before the swap
print("Before")
print(printInOrder(root1, []))

solution = Solution()
solution.recoverTree(root1)

#print after the swap
print("After")
print(printInOrder(root1, []))
