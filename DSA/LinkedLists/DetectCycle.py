# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:46:21 2018

@author: Nirav Modi

Detect Cycle in a linked list
"""


def detectCycle(head):
    
    if head is None:
        return False
    if head.next is None:
        return False
    if head.next.next is None:
        return False

    slowRunner = head
    fastRunner = head.next.next
    
    while(fastRunner is not None):
        
        if fastRunner.next is None:
            return False
        
        if slowRunner == fastRunner:
            return True
        
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next.next
        
    return False