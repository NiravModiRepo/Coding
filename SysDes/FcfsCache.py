# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:29:45 2018

@author: Nirav Modi

First come first serve cache

https://www.youtube.com/watch?v=UTXkbcJUY74&t=233s
https://www.youtube.com/watch?v=HIB3hZ-5fHw


"""

class Node:
    def __init__ (self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class FcfsCache:
    def __init__ (self, cap):
        self.cap = cap # initialize user requested cap
        self.size = 0 # size initialized at 0, will increment, once it grows
        self.dict = {} # dictionary for all nodes, it will only hold capacity nodes
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        # Merge head and tail together
        # Every node will be in between
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        if key in self.dict:
            if self.dict[key] is not None:
                return self.dict[key].val # key is found in cache
        return -1 #key not found in cache
    
    def put(self, key, val):
        #add key in cache
        if self.get(key) > 0:
            self.dict[key].val = val
            return
        
        #if cache is not full, incremenent the size
        if self.size < self.cap:
            self.size += 1
        else:
            #find last node to remove
            n = self.tail.prev
            #if cache is full, remove the tail to make room
            self._remove()
            #free up space in the cache
            del self.dict[n.key]
        
        # add the new value to the cache
        self._add(key,val)
        
        return
    
    def _remove(self):
        
        #Find node to remove
        n = self.tail.prev
        # Bridge previous node and tail
        n.prev.next = self.tail
        # Bridge tail and previous node
        self.tail.prev = n.prev
    
    def _add(self, key, val):
        
        # Initialize new node
        n = Node(key, val)
        # bridge new node to next node
        n.next = self.head.next
        # bridge head to new node
        self.head.next = n
        # bridge new node to head
        n.prev = self.head
        # bridge next node to new node
        n.next.prev = n
        # add node to cache
        self.dict[key] = n
        
        
fcfs = FcfsCache(4)

array = [1,2,3,4,1,2,5,1,2,3]
outputArray = []

for i in array:
    x = fcfs.get(i)
    outputArray.append(x)
    if x < 0:
        fcfs.put(i, i)

print(outputArray)

