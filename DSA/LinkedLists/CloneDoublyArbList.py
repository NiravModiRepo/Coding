# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:16:05 2018

Clone a doubly linked list with next and an arbitrary pointer

This would be O(n) time and O(n) space because of the stack

@author: nam42589
"""

class ArbDoublyListNode:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.arb = None
       
    def insertNodeNext(self, node):
        self.next = node
   
    def insertNodeArb(self, node):
        self.arb = node
       

def cloneSinglyList(node):
   
    if node is None:
        return
   
    nodeCopy = ArbDoublyListNode(node.value)
    nodeCopy.next = cloneSinglyList(node.next)
    nodeCopy.arb = node
    node.next = nodeCopy
   
    return nodeCopy
   
def updateArbPointers(nodeCopy):
    
    if nodeCopy is None:
        return
    
    nodeCopy.arb = nodeCopy.arb.arb.next
    
    updateArbPointers(nodeCopy.next)
    
    return
    

def cloneDoublyArbList(root):
   
    if root is None:
        return
    
    rootCopy = cloneSinglyList(root)  
    updateArbPointers(rootCopy)
    
    return rootCopy



   
first = ArbDoublyListNode(1)
second = ArbDoublyListNode(2)
third = ArbDoublyListNode(3)
fourth = ArbDoublyListNode(4)

first.insertNodeNext(second)
second.insertNodeNext(third)
third.insertNodeNext(fourth)

first.insertNodeArb(third)
second.insertNodeArb(fourth)
third.insertNodeArb(first)
fourth.insertNodeArb(second)

head = cloneDoublyArbList(first)

