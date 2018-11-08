# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:09:21 2018

@author: Nirav Modi
"""

import multiprocessing

def calc_square(numbers, result, value):
    
    print("Within Process: Calculating Squares")
    for index, n in enumerate(numbers):
        result[index] = n**2
    value.value = index

if __name__ == "__main__":
    arr = [2,3,5]
    
    result = multiprocessing.Array('i',3)
    value = multiprocessing.Value('d',0.0)
    
    p1 = multiprocessing.Process(target=calc_square, args=(arr,result, value))

    p1.start()

    p1.join()


    print("Outside Process: ", result[:], value.value)