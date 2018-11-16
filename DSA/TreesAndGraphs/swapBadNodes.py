# -*- coding: utf-8 -*-
"""
Binary Search Tree has 2 nodes that are swapped

Swap them back

@author: Nirav Modi

https://leetcode.com/problems/recover-binary-search-tree/description/

O(n) space -> InOrder Trav
O(1) space -> Morris Trav
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
        
        #empty array for all nodes        
        array = []
        
        #invalid tree
        if root is None:
            return root
        
        #Record entries in the array, takes O(n) time and space
        self.inOrderRecord(root, array)
        
        #prev node is initialized for reference
        prev = TreeNode(-float('inf'))
        
        #flag to take the first or second value when its not in order
        flag = True
        
        #swap nodes array, must max out at 2
        badNodes = []
        
        for i in array:
            
            #if previous is greater than current
            if prev.val > i.val:
                if flag:
                    #add both values in bad nodes in case they are next to each other
                    badNodes.append(prev)
                    badNodes.append(i)
                    flag = False
                else:
                    #add last entry in bad nodes
                    badNodes[1] = i
                    break
                    
            #current becomes previous        
            prev = i
                    
        badNodes[1].val, badNodes[0].val = badNodes[0].val, badNodes[1].val                
        
        return
        
    # In Order Traversal that adds values to the aray
    def inOrderRecord(self, node, array):
        
        #Reached end, go up
        if node is None:
            return
        
        #go left first because that is the smaller value
        self.inOrderRecord(node.left, array)
        
        #print node
        array.append(node)
        
        #go right after
        self.inOrderRecord(node.right, array)
        
        return
    
            
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


    
