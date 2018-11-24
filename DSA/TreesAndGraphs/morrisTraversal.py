# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 22:48:46 2018

@author: Nirav Modi

Morris Traversal

                7
        5               4
    8       6
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

#Problem from Video    
root = TreeNode(7)
root.left = TreeNode(5)
root.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(8)

def morrisTrav(root):
    
    initFlag = True
    noErrorFlag = True
    notDoneFlag = True
    badNodes = []
    current = root
    
    while (current is not None):
        if current.left is None: 
            print(current.val) 
            ##################################
            if initFlag:
                prev = current
                initFlag = False
            elif notDoneFlag:
                if current.val < prev.val:
                    if noErrorFlag:
                        badNodes.append(prev)
                        badNodes.append(current)
                        noErrorFlag = False
                    else:
                        badNodes[1] = current
                        notDoneFlag = False
            prev = current
            ##################################
                
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
                ##################################
                if initFlag:
                    prev = current
                    initFlag = False
                elif notDoneFlag:
                    if current.val < prev.val:
                        if noErrorFlag:
                            badNodes.append(prev)
                            badNodes.append(current)
                            noErrorFlag = False
                        else:
                            badNodes[1] = current
                            notDoneFlag = False
                prev = current
                ##################################
                current = current.right 
    
    if len(badNodes):
        badNodes[0].val, badNodes[1].val = badNodes[1].val, badNodes[0].val
    
    return root

#Print before the swap
print("Before")
print(printInOrder(root, []))

morrisTrav(root)

#print after the swap
print("After")
print(printInOrder(root, []))