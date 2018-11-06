# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:47:44 2018

Connect Nodes at the same level in a binary tree

Input:


    A
   / \
  B    C
 /\   /\
D  E  F G

Output:
    
    A---------None
   / \
  B---C-------None
 /\   /\
D--E-F--G-----None



@author: Nirav Modi

LeetCode: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
"""

class BinaryTreeNextNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None
    
    def insert_left(self, value):
        self.left = BinaryTreeNextNode(value)
        return self.left
    
    def insert_right(self, value):
        self.right = BinaryTreeNextNode(value)
        return self.right
    
    def insert_next_node(self, node):
        self.next = node
        return


def connectRightNode(root):
    
    if root is None:
        return root
    
    #set up the queue for BFS, list includes node and depth
    nodes = [(root, 0)]
    
    #Have to start at queue depth -1
    prevDepth = -1
    #prev node initialized at Null pointer
    prevNode = None
    
    #add and remove to the queue
    while (len(nodes)):
        
        #next node
        node, depth = nodes.pop(0)
        
        #if depth is same, link the previous node
        if prevDepth == depth:
            prevNode.next = node
            
        #append node with depth
        if node.left is not None:
            nodes.append((node.left, depth+1))
        
        #append node with depth
        if node.right is not None:
            nodes.append((node.right, depth+1))
            
        #set current node and depth to previous
        prevNode = node
        prevDepth = depth


root = BinaryTreeNextNode('A')
left = root.insert_left('B')
right = root.insert_right('C')
left_left = left.insert_left('D')
left_right = left.insert_right('E')
right_left = right.insert_left('F')
right_right = right.insert_right('G')

connectRightNode(root)