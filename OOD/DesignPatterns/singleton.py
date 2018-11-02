# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:15:17 2018

@author: Nirav Modi

Singleton Design Patterns

https://www.youtube.com/watch?v=6IV_FYx6MQA
"""

class MySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 10
        return self._instance

x = MySingleton()
print(x.y)

x.y = 20

z = MySingleton()
print(z.y)

#######################################################
#Singleton decorator

def singleton(myClass):
    instances = {}
    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstance

@singleton
class TestClass(object):
    pass

x = TestClass()