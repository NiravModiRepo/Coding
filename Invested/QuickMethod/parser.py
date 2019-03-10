# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:09:04 2019

@author: nam42589
"""


import requests

#page = requests.get('https://finance.yahoo.com/quote/goog/')
#string = page.text

#x = string.find('EPS (TTM)')
#
#y = string[x:x+200]
#
#valueStr = ""
#print(y)
#
#count = 0
#for i in range(len(y)):
#    
#    searchString = 'data-reactid'
#    z = y[i:i+len(searchString)] 
#    
#    if (z == searchString) and (count > 0):
#        print(i)
#        a = i+len(searchString)+6
#        while ((y[a].isdigit()) or (y[a] == ".") or (y[a] == ",")) :
#            valueStr+=y[a]
#            a+=1
#            
#            
#    if (z == searchString):
#        count+=1
#        
#print("EPS = ", valueStr)



#x = string.find('Previous Close')
#
#y = string[x:x+200]
#
#valueStr = ""
#print(y)
#
#count = 0
#for i in range(len(y)):
#    
#    searchString = 'data-reactid'
#    z = y[i:i+len(searchString)] 
#    
#    if (z == searchString) and (count > 0):
#        print(i)
#        a = i+len(searchString)+6
#        while ((y[a].isdigit()) or (y[a] == ".") or (y[a] == ",")) :
#            valueStr+=y[a]
#            a+=1
#            
#            
#    if (z == searchString):
#        count+=1
#        
#print("Previous Close = ", valueStr)


#page = requests.get('https://finance.yahoo.com/quote/aapl/analysis/')
#string = page.text
#
#x = string.find('Next 5 Years (per annum)')
#
#y = string[x:x+100]
#
#valueStr = ""
#print(y)
#
#count = 1
#for i in range(len(y)):
#    
#    searchString = 'data-reactid'
#    z = y[i:i+len(searchString)] 
#    
#    if (z == searchString) and (count > 0):
#        print(i)
#        a = i+len(searchString)+7
#        while ((y[a].isdigit()) or (y[a] == ".") or (y[a] == ",")) :
#            valueStr+=y[a]
#            a+=1
#            
#            
#    if (z == searchString):
#        count+=1
#        
#print("Next 5 Years (per annum) = ", valueStr)
#


page = requests.get('https://www.macrotrends.net/stocks/charts/nflx/netflix/total-share-holder-equity')
string = page.text