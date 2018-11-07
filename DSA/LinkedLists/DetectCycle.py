# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:46:21 2018

@author: Nirav Modi

Detect Cycle in a linked list
"""


def detectCycle(head):
    
    #if head is none return false and validate runner node
    if head is None:
        return False
    if head.next is None:
        return False
    if head.next.next is None:
        return False

    #initialzie both runners
    slowRunner = head
    fastRunner = head.next.next
    
    #iterate runner, while its not none
    while(fastRunner is not None):
        
        #reached end
        if fastRunner.next is None:
            return False
        
        #reached same node, found cycle
        if slowRunner == fastRunner:
            return True
        
        #iterate runner, fast runner moves twice
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next.next
        
    return False