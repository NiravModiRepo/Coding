# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:01:52 2018

@author: Nirav Modi

Multiprocessing Introduction
https://www.youtube.com/watch?v=Lu5LrKh1Zno&index=2&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN
"""

import multiprocessing

square_result = []

def calc_square(numbers):
    
    global square_result
    print("Calculating Squares")
    for i in numbers:
        print("square: " + str(i**2))
        square_result.append(i**2)
    print("Within Process Result: " + str(square_result))

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))

    p1.start()

    p1.join()


    print("Result: " + str(square_result))
    print("Done!")