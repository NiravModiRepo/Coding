# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:16:05 2018

Clone a doubly linked list with next and an arbitrary pointer

This would be O(n) time and O(n) space because of the stack

@author: nam42589
"""

# Arbitrary Linked List Node
class ArbDoublyListNode:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.arb = None
       
    def insertNodeNext(self, node):
        self.next = node
   
    def insertNodeArb(self, node):
        self.arb = node
       

#Clones the singly list and modifies the node copy
def cloneSinglyList(node):
   
    #end of list, go back!
    if node is None:
        return
    
    #Creates Copy Node
    nodeCopy = ArbDoublyListNode(node.value)
    
    #Recursively goes to the next node
    nodeCopy.next = cloneSinglyList(node.next)
    
    #This could be before or after the recursive call
    nodeCopy.arb = node
    
    #modifies the next node after the recursive call
    node.next = nodeCopy
   
    #returns the copy up the stack
    return nodeCopy
   
def updateArbPointers(nodeCopy):
    
    #end of list, go back!
    if nodeCopy is None:
        return
    
    #Update Arb pointer to point correctly
    nodeCopy.arb = nodeCopy.arb.arb.next
    
    #Recurse Down
    updateArbPointers(nodeCopy.next)
    
    #Recurse Up
    return
    

def cloneDoublyArbList(root):
   
    #end of list, go back!
    if root is None:
        return
    
    #Clones singly list and makes copies of nodes
    rootCopy = cloneSinglyList(root)  
    
    #Update the Arbitrary pointers
    updateArbPointers(rootCopy)
    
    #return to function call
    return rootCopy


#This would take O(n) time and O(1) space
#This method would inject copies in between the nodes    
def iterCloneDoublyArbList(root):
    
    if root is None:
        return root
    
    #runnder node
    runnerNode = root
    
    #iterate through list and make copies next to it
    # 1->2->3->4 to 1->1'->2->2'->3->3'->4->4'
    while (runnerNode is not None):
        
        #store next node
        nextNode = runnerNode.next
        
        #Create node in between
        runnerNode.next = ArbDoublyListNode(runnerNode.value)
        
        #finish putting the copied node in between
        runnerNode.next.next = nextNode
        
        #update runnerNode
        runnerNode = nextNode
    
    #update runner node for next loop
    runnerNode = root
    
    #Iterate through list and assign arbitrary pointers
    while(runnerNode is not None):
        
        #Update arbitrary pointers for copy nodes
        runnerNode.next.arb = runnerNode.arb.next if runnerNode.arb else None
        
        #go to next node
        runnerNode = runnerNode.next.next

    #update head of copied root
    copyRoot = root.next    
    
    #update runner node for next loop
    runnerNode = root
    runnerCopyNode = copyRoot
    
    #Interate through the list and unweave the lists
    #1->1'->2->2'->3->3'->4->4' to 1->2->3->4 and 1'->2'->3'->4'
    while(runnerNode is not None):
        
        runnerNode.next = runnerNode.next.next        
        runnerCopyNode.next = runnerCopyNode.next.next if runnerCopyNode.next else None
        
        runnerNode = runnerNode.next
        runnerCopyNode = runnerCopyNode.next

    return copyRoot

   
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

#head = cloneDoublyArbList(first)

head = iterCloneDoublyArbList(first)

