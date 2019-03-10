# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:03:18 2019

@author: Nirav Modi
"""

import requests

globalSymList = ['AAPL', 'GOOG', 'GOOGL', 'FB', 'AMZN', 'MSFT', 'NFLX', 'DIS', 'AMD', 'IBM']
globalMainWeb = ""
globalAnalystWeb = ""

def Get_Curr_Price(sym):
    
    page = requests.get(globalMainWeb)
    string = page.text
    
    x = string.find('Previous Close')
    
    y = string[x:x+200]
    
    valueStr = ""
    
    count = 0
    for i in range(len(y)):
        
        searchString = 'data-reactid'
        z = y[i:i+len(searchString)] 
        
        if (z == searchString) and (count > 0):
            a = i+len(searchString)+6
            while ((y[a].isdigit()) or (y[a] == ".") or (y[a] == ",")) :
                valueStr+=y[a]
                a+=1
                
                
        if (z == searchString):
            count+=1
    
    valueStr = valueStr.replace(",","")
    return float(valueStr)

def Get_Eps(sym):
    
    # https://finance.yahoo.com/quote/aapl/
    # EPS-TTM
    
    page = requests.get(globalMainWeb)
    string = page.text
    
    x = string.find('EPS (TTM)')
    
    y = string[x:x+200]
    
    valueStr = ""
    
    count = 0
    for i in range(len(y)):
        
        searchString = 'data-reactid'
        z = y[i:i+len(searchString)] 
        
        if (z == searchString) and (count > 0):
            a = i+len(searchString)+6
            while ((y[a].isdigit()) or (y[a] == ".") or (y[a] == ",")) :
                valueStr+=y[a]
                a+=1
                
                
        if (z == searchString):
            count+=1
    
    valueStr = valueStr.replace(",","")
    return float(valueStr)

def Get_Wind_Analyst(sym):
    
    page = requests.get(globalAnalystWeb)
    string = page.text
    
    x = string.find('Next 5 Years (per annum)')
    
    y = string[x:x+100]
    
    valueStr = ""
    
    count = 1
    for i in range(len(y)):
        
        searchString = 'data-reactid'
        z = y[i:i+len(searchString)] 
        
        if (z == searchString) and (count > 0):
            a = i+len(searchString)+7
            while ((y[a].isdigit()) or (y[a] == ".") or (y[a] == ",")) :
                valueStr+=y[a]
                a+=1
                
                
        if (z == searchString):
            count+=1
            
        valueStr = valueStr.replace(",","")
    return float(valueStr)

def Get_Wind_Hist(sym):
    
    return 99999

def Get_Pe_Max(sym):
    
    return 99999

def Get_Wind_Growth_Rate(sym):
    
    #Get Historical Windage Growth Rate
    #Get Analyst Windage Growth Rate
    #Return min
    return min (Get_Wind_Hist(sym), Get_Wind_Analyst(sym))

def Get_Windage_Pe_Ratio(sym, windOverall):
    
    return min(2*windOverall, Get_Pe_Max(sym))

def Get_Future_Eps(eps, windOverall):
    
    futureEps = eps
    for i in range(0,10):
        futureEps *= (1+(windOverall/100))
        #print("Year", i, "Price: ", futureEps)
    
    return futureEps
    
def Get_Mos_Price(sym):
    
    #Step 0 - Setup: Acquire numbers needed
    
    #Get EPS
    eps = Get_Eps(sym)
    #print("EPS = ", eps)
    
    #Get the overall Windage Growth Rate
    windOverall = Get_Wind_Growth_Rate(sym)
    #print("Windage Overall = ", windOverall)
    
    #Get Windage Price to Earnings Ratio
    windPeRatio = Get_Windage_Pe_Ratio(sym, windOverall)
    #print("Windage PE Ratio = ", windPeRatio)
    
    #Step 1 - Future 10 year EPS
    futureEps = Get_Future_Eps(eps, windOverall)
    #print("Future EPS = ", futureEps)
    
    #Step 2 - Future 10 year share price
    future10YearSharePrice = futureEps * windPeRatio
    #print("Future 10 Year Price = ", future10YearSharePrice)
    
    #Step 3 - Sticker Price
    stickerPrice = future10YearSharePrice / 4
    #print("Sticker Price = ", stickerPrice)
    
    #Step 4 - Margin of Safety Price
    mosPrice = stickerPrice / 2
    #print("Margin of Safety Price = ", mosPrice)
    
    return round(mosPrice, 2)

for sym in globalSymList:
    mosPrice = 0
    currPrice = 0
    globalMainWeb = 'https://finance.yahoo.com/quote/'+sym+'/'
    globalAnalystWeb = 'https://finance.yahoo.com/quote/'+sym+'/analysis/'
    
    mosPrice = Get_Mos_Price(sym)
    currPrice = Get_Curr_Price(sym)
    
    print("Symbol =", sym, "\tMargin Of Safety =", mosPrice, "\tCurrent =", currPrice)
    
    if(mosPrice >= currPrice):
        print("\t\t\t\tBUY")