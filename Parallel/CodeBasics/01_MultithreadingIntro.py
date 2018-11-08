# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:45:38 2018

@author: Nirav Modi

Multithreading Introduction
https://www.youtube.com/watch?v=PJ4t2U15ACo
"""
import time
import threading

def calc_square(numbers):
    
    print("Calculating Squares")
    for i in numbers:
        time.sleep(0.2)
        print("square: ", i**2)
        
def calc_cube(numbers):
    
    print("Calculating Cubes")
    for i in numbers:
        time.sleep(0.2)
        print("cube: ", i**3)
        
        
numbers = [2,3,8,9]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(numbers,))
t2 = threading.Thread(target=calc_cube, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()
"""
calc_square(numbers)
calc_cube(numbers)
"""
print("Finished the task in ", (time.time()-t))
        
