# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 23:01:04 2018

@author: Nirav Modi
"""

from multiprocessing import Pool
import time

def f(n):
    
    sum = 0
    for x in range(100):
        sum+= x*x
        
    return sum

if __name__ == "__main__":
    
    array = [1,2,3,4,5]
    
    t1 = time.time()
    p = Pool(processes=3)
    #result = p.map(f, array)
    result = p.map(f, range(1000000))
    p.close()
    p.join()
    
    print("Pool took: ", time.time()-t1)
    
    t2 = time.time()
    
    result = []
    for x in range(1000000):
        result.append(f(x))
        
        
    print("Serial took: ", time.time()-t2)    
        
#    result = []
#    
#    for n in array:
#        result.append(f(n))
        
#    print(result)