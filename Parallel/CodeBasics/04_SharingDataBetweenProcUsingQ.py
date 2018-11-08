# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:23:44 2018

@author: Nirav Modi
"""

import multiprocessing

def calc_square(numbers, queue):
    
    global square_result
    print("Calculating Squares")
    for i in numbers:
        queue.put(i**2)
        
        
if __name__ == "__main__":
    arr = [2,3,8]
    q1 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,q1))

    p1.start()

    p1.join()


    while(q1.empty() is False):
        print(q1.get())
        
    print("Done!")