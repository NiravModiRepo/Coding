# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:24:29 2018

@author: Nirav Modi

Source: https://hackernoon.com/synchronization-primitives-in-python-564f89fee732
"""

#rlock_tut.py

import threading

num = 0


"""
lock = threading.Lock()

lock.acquire()
num += 1
lock.acquire() # This will block.
num += 2
lock.release()
"""

# With RLock, that problem doesn’t happen.
lock = threading.RLock()

lock.acquire()
num += 3
lock.acquire() # This won’t block.
num += 4
lock.release()
lock.release() # You need to call release once for each call to acquire.