# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:32:44 2019

@author: nam42589
"""

def GetGrowthRate(x, arr):
    
    growingSum = 0
    
    for i in range(0,x):
        growingSum += arr[i]
        
    return growingSum/x

def GetYearlyGrowth(arr):
    
    yearlyArr = [0]*(len(arr)-1)
    
	
    for i in range(0,len(yearlyArr)):
        z = 0
        x = arr[i]
        y = arr[i+1]
        if (y):
            z = ((x*100)/y)-100
        yearlyArr[i] = z  
        
    return yearlyArr
    

dataNetIncome = []
dataTotalEquity = []
dataDividends = []
dataNetSales = []
dataCashGenerated = []

#DATA_ENTRY Net Income from Income Statement
#https://www.macrotrends.net/stocks/charts/FIZZ/national-beverage/net-income
dataNetIncome.append(150)
dataNetIncome.append(107)
dataNetIncome.append(61)
dataNetIncome.append(49)
dataNetIncome.append(43)
dataNetIncome.append(47)
dataNetIncome.append(44)
dataNetIncome.append(41)
dataNetIncome.append(33)
dataNetIncome.append(25)
dataNetIncome.append(22)

#DATA_ENTRY Equity from Balance Sheet
#https://www.macrotrends.net/stocks/charts/FIZZ/national-beverage/total-share-holder-equity
dataTotalEquity.append(331)
dataTotalEquity.append(246)
dataTotalEquity.append(206)
dataTotalEquity.append(148)
dataTotalEquity.append(106)
dataTotalEquity.append(70)
dataTotalEquity.append(122)
dataTotalEquity.append(80)
dataTotalEquity.append(142)
dataTotalEquity.append(170)
dataTotalEquity.append(145)

#DATA_ENTRY Dividends from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/FIZZ/national-beverage/common-stock-dividends-paid
dataDividends.append(-70)
dataDividends.append(-70)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(-118)
dataDividends.append(0)
dataDividends.append(-106)
dataDividends.append(-62)
dataDividends.append(0)
dataDividends.append(-37)

#DATA_ENTRY Sales from Income Statement
#https://www.macrotrends.net/stocks/charts/FIZZ/national-beverage/revenue
dataNetSales.append(976)
dataNetSales.append(827)
dataNetSales.append(705)
dataNetSales.append(646)
dataNetSales.append(641)
dataNetSales.append(662)
dataNetSales.append(629)
dataNetSales.append(600)
dataNetSales.append(593)
dataNetSales.append(575)
dataNetSales.append(566)

#DATA_ENTRY Operating Cash from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/FIZZ/national-beverage/cash-flow-from-operating-activities
dataCashGenerated.append(155)
dataCashGenerated.append(114)
dataCashGenerated.append(80)
dataCashGenerated.append(58)
dataCashGenerated.append(52)
dataCashGenerated.append(40)
dataCashGenerated.append(38)
dataCashGenerated.append(55)
dataCashGenerated.append(54)
dataCashGenerated.append(36)
dataCashGenerated.append(34)

#DATA_ENTRY EPS
#https://www.macrotrends.net/stocks/charts/FIZZ/national-beverage/eps-earnings-per-share-diluted
eps = 3.19

#DATA_ENTRY Highest PE Ratio from last 10 years
#https://www.macrotrends.net/stocks/charts/FIZZ/national-beverage/pe-ratio
highestPeRatio = 39.51

#DATA_ENTRY
#https://finance.yahoo.com/quote/fizz/analysis/
#Grwoth Estimates - Next 5 Years (per annum)
analystWindageRate = 25.56

############################################################

#yearlyGrowthNetIncome = [0]*(len(dataNetIncome)-1)
#
##get growth of yearly net income
#for i in range(0,len(yearlyGrowthNetIncome)):
#    x = dataNetIncome[i]
#    y = dataNetIncome[i+1]
#    z = ((x*100)/y)-100
#    yearlyGrowthNetIncome[i] = z

yearlyGrowthNetIncome = GetYearlyGrowth(dataNetIncome) 

growthRate3YearNetIncome = GetGrowthRate(3, yearlyGrowthNetIncome)
growthRate5YearNetIncome = GetGrowthRate(5, yearlyGrowthNetIncome)
growthRate10YearNetIncome = GetGrowthRate(10, yearlyGrowthNetIncome)

#print(growthRate3YearNetIncome)
#print(growthRate5YearNetIncome)
#print(growthRate10YearNetIncome)
############################################################

dataEquityPlusDividends = []

for i in range(0,len(dataTotalEquity)):
    dataEquityPlusDividends.append(dataTotalEquity[i]+dataDividends[i])
    
#yearlyGrowthEquityPlusDividends = [0]*(len(dataEquityPlusDividends)-1)
#
#get growth of yearly Equity Plus Dividends
#for i in range(0,len(yearlyGrowthEquityPlusDividends)):
#    x = dataEquityPlusDividends[i]
#    y = dataEquityPlusDividends[i+1]
#    z = ((x*100)/y)-100
#    yearlyGrowthEquityPlusDividends[i] = z    
    
yearlyGrowthEquityPlusDividends = GetYearlyGrowth(dataEquityPlusDividends) 
   
growthRate3YearEquityPlusDividends = GetGrowthRate(3, yearlyGrowthEquityPlusDividends)
growthRate5YearEquityPlusDividends = GetGrowthRate(5, yearlyGrowthEquityPlusDividends)
growthRate10YearEquityPlusDividends = GetGrowthRate(10, yearlyGrowthEquityPlusDividends)

#print(growthRate3YearEquityPlusDividends)
#print(growthRate5YearEquityPlusDividends)
#print(growthRate10YearEquityPlusDividends)
############################################################    
    
#yearlyGrowthNetSales = [0]*(len(dataNetSales)-1)
#
##get growth of yearly net sales
#for i in range(0,len(yearlyGrowthNetSales)):
#    x = dataNetSales[i]
#    y = dataNetSales[i+1]
#    z = ((x*100)/y)-100
#    yearlyGrowthNetSales[i] = z
    
yearlyGrowthNetSales = GetYearlyGrowth(dataNetSales)    

growthRate3YearNetSales = GetGrowthRate(3, yearlyGrowthNetSales)
growthRate5YearNetSales = GetGrowthRate(5, yearlyGrowthNetSales)
growthRate10YearNetSales = GetGrowthRate(10, yearlyGrowthNetSales)

#print(growthRate3YearNetSales)
#print(growthRate5YearNetSales)
#print(growthRate10YearNetSales)
############################################################    
    
#yearlyGrowthCashGenerated = [0]*(len(dataCashGenerated)-1)

#get growth of yearly cash generated
#for i in range(0,len(yearlyGrowthCashGenerated)):
#    x = dataCashGenerated[i]
#    y = dataCashGenerated[i+1]
#    z = ((x*100)/y)-100
#    yearlyGrowthCashGenerated[i] = z 
yearlyGrowthCashGenerated = GetYearlyGrowth(dataCashGenerated)     

growthRate3YearCashGenerated = GetGrowthRate(3, yearlyGrowthCashGenerated)
growthRate5YearCashGenerated = GetGrowthRate(5, yearlyGrowthCashGenerated)
growthRate10YearCashGenerated = GetGrowthRate(10, yearlyGrowthCashGenerated)

#print(growthRate3YearCashGenerated)
#print(growthRate5YearCashGenerated)
#print(growthRate10YearCashGenerated)
############################################################

windageNetIncome = (growthRate3YearNetIncome + growthRate5YearNetIncome + growthRate10YearNetIncome)/3
windageEquityPlusDividends = (growthRate3YearEquityPlusDividends + growthRate5YearEquityPlusDividends + growthRate10YearEquityPlusDividends)/3
windageNetSales = (growthRate3YearNetSales + growthRate5YearNetSales + growthRate10YearNetSales)/3
windageCashGenerated = (growthRate3YearCashGenerated + growthRate5YearCashGenerated + growthRate10YearCashGenerated)/3
  
windageRate = (windageNetIncome + windageEquityPlusDividends + windageNetSales + windageCashGenerated)/4
print("Overall Windage Rate: ", windageRate)
print("\n")

windageGrowthRate = min(windageRate, analystWindageRate)

########################################################################################################################
futureEps = eps

windagePercent = windageGrowthRate/100

print("Windage PE Ratio: Min of 2xWindage Rate:", 2*windageGrowthRate, ", Highest PE Ratio: ", highestPeRatio)
windagePeRatio = min(2*windageGrowthRate, highestPeRatio)
print("\n")

########################################################################################################################
#Whole foods
#futureEps = 1.48
#windagePercent = 0.14
#windagePeRatio = 28

print("windagePercent: ", windagePercent)

#Step One
for i in range(0,10):
    futureEps *= (1+windagePercent)
    print("Year", i, "Price: ", futureEps)

print("\n")
    
print("Step One: Future EPS: ", futureEps)

#Step Two
future10YearSharePrice = futureEps * windagePeRatio
print("Step Two: Future 10 Year Share Price: ", future10YearSharePrice)

#Step Three
stickerPrice = future10YearSharePrice / 4
print("Step Three: Sticker Price: ", stickerPrice)

#Step Four
marginOfSafetyPrice = stickerPrice/2
print("Step Four: Margin Of Safety Price: ", marginOfSafetyPrice)