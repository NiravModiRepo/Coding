# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:31:55 2018

@author: Nirav Modi
"""

class OperatingSystem:
    multitasking = True
    name = "Mac OS"
    
class Apple:
    website = "www.apple.com"
    name = "Apple"
    
	

#First class will be taken
class MacBook(Apple, OperatingSystem):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more details".format(self.website))
            print("Name: ", self.name)
        
macBook = MacBook()