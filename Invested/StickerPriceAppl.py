# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:48:25 2019

@author: Nirav

May Practice - Windage Rate

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
#https://www.macrotrends.net/stocks/charts/AAPL/apple/net-income
dataNetIncome.append(59531)
dataNetIncome.append(48351)
dataNetIncome.append(45687)
dataNetIncome.append(53394)
dataNetIncome.append(39510)
dataNetIncome.append(37037)
dataNetIncome.append(41733)
dataNetIncome.append(25922)
dataNetIncome.append(14013)
dataNetIncome.append(8235)
dataNetIncome.append(6119)

#DATA_ENTRY Equity from Balance Sheet
#https://www.macrotrends.net/stocks/charts/AAPL/apple/total-share-holder-equity
dataTotalEquity.append(107147)
dataTotalEquity.append(134047)
dataTotalEquity.append(128249)
dataTotalEquity.append(119355)
dataTotalEquity.append(111547)
dataTotalEquity.append(123549)
dataTotalEquity.append(118210)
dataTotalEquity.append(76615)
dataTotalEquity.append(47791)
dataTotalEquity.append(31640)
dataTotalEquity.append(22297)

#DATA_ENTRY Dividends from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/AAPL/apple/common-stock-dividends-paid
dataDividends.append(13712)
dataDividends.append(12769)
dataDividends.append(12150)
dataDividends.append(11561)
dataDividends.append(11126)
dataDividends.append(10564)
dataDividends.append(2488)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)

#DATA_ENTRY Sales from Income Statement
#https://www.macrotrends.net/stocks/charts/AAPL/apple/revenue
dataNetSales.append(265595)
dataNetSales.append(229234)
dataNetSales.append(215639)
dataNetSales.append(233715)
dataNetSales.append(182795)
dataNetSales.append(170910)
dataNetSales.append(156508)
dataNetSales.append(108249)
dataNetSales.append(65225)
dataNetSales.append(42905)
dataNetSales.append(37491)

#DATA_ENTRY Operating Cash from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/AAPL/apple/cash-flow-from-operating-activities
dataCashGenerated.append(77434)
dataCashGenerated.append(64225)
dataCashGenerated.append(66231)
dataCashGenerated.append(81266)
dataCashGenerated.append(59713)
dataCashGenerated.append(53666)
dataCashGenerated.append(50856)
dataCashGenerated.append(37529)
dataCashGenerated.append(18595)
dataCashGenerated.append(10159)
dataCashGenerated.append(9596)

#DATA_ENTRY EPS
#https://www.macrotrends.net/stocks/charts/AAPL/apple/eps-earnings-per-share-diluted
eps = 11.91

#DATA_ENTRY Highest PE Ratio from last 10 years
#https://www.macrotrends.net/stocks/charts/AAPL/apple/pe-ratio
highestPeRatio = 20.70

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

windageNetIncome = (growthRate3YearNetIncome + growthRate5YearNetIncome)/2
windageEquityPlusDividends = (growthRate3YearEquityPlusDividends + growthRate5YearEquityPlusDividends)/2
windageNetSales = (growthRate3YearNetSales + growthRate5YearNetSales)/2
windageCashGenerated = (growthRate3YearCashGenerated + growthRate5YearCashGenerated)/2
    
windageRate = (windageNetIncome + windageEquityPlusDividends + windageNetSales + windageCashGenerated)/4
print("Overall Windage Rate: ", windageRate)
print("\n")

########################################################################################################################
futureEps = eps

windagePercent = windageRate/100

print("Windage PE Ratio: Min of 2xWindage Rate:", 2*windageRate, ", Highest PE Ratio: ", highestPeRatio)
windagePeRatio = min(2*windageRate, highestPeRatio)
print("\n")


########################################################################################################################
#Whole foods
#futureEps = 1.48
#windagePercent = 0.14
#windagePeRatio = 28

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