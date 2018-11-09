# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:46:00 2018

@author: Nirav Modi

Source: https://hackernoon.com/synchronization-primitives-in-python-564f89fee732
"""

#barrier_tut.py

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num = 4
# 4 threads will need to pass this barrier to get released.
b = Barrier(num)
names = ["Harsh", "Lokesh", "George", "Iqbal"]

def player():
    name = names.pop()
    sleep(randrange(2, 5))
    print("%s reached the barrier at: %s" % (name, ctime()))
    b.wait()
    
threads = []
print("Race starts now…")

for i in range(num):
    threads.append(Thread(target=player))
    threads[-1].start()

"""
Following loop enables waiting for the threads to complete before moving on with the main script.
"""

for thread in threads:
    thread.join()
print()
print("Race over!")