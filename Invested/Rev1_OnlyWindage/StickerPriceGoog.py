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
# https://www.macrotrends.net/stocks/charts/GOOG/google/net-income
dataNetIncome.append(30736)
dataNetIncome.append(12662)
dataNetIncome.append(19478)
dataNetIncome.append(15826)
dataNetIncome.append(14136)
dataNetIncome.append(12733)
dataNetIncome.append(10737)
dataNetIncome.append(9737)
dataNetIncome.append(8505)
dataNetIncome.append(6520)
dataNetIncome.append(4227)

#DATA_ENTRY Equity from Balance Sheet
# https://www.macrotrends.net/stocks/charts/GOOG/google/total-share-holder-equity
dataTotalEquity.append(177628)
dataTotalEquity.append(152502)
dataTotalEquity.append(139036)
dataTotalEquity.append(120331)
dataTotalEquity.append(103860)
dataTotalEquity.append(87309)
dataTotalEquity.append(71715)
dataTotalEquity.append(58145)
dataTotalEquity.append(46241)
dataTotalEquity.append(36004)
dataTotalEquity.append(28239)

#DATA_ENTRY Dividends from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/GOOG/google/common-stock-dividends-paid
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)
dataDividends.append(0)

#DATA_ENTRY Sales from Income Statement
#https://www.macrotrends.net/stocks/charts/GOOG/google/revenue
dataNetSales.append(136819)
dataNetSales.append(110855)
dataNetSales.append(90272)
dataNetSales.append(74989)
dataNetSales.append(66001)
dataNetSales.append(55519)
dataNetSales.append(46039)
dataNetSales.append(37905)
dataNetSales.append(29321)
dataNetSales.append(23651)
dataNetSales.append(21796)

#DATA_ENTRY Operating Cash from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/GOOG/google/cash-flow-from-operating-activities
dataCashGenerated.append(47971)
dataCashGenerated.append(37091)
dataCashGenerated.append(36036)
dataCashGenerated.append(26572)
dataCashGenerated.append(23024)
dataCashGenerated.append(18659)
dataCashGenerated.append(16619)
dataCashGenerated.append(14565)
dataCashGenerated.append(11081)
dataCashGenerated.append(9316)
dataCashGenerated.append(7853)

#DATA_ENTRY EPS
#https://www.macrotrends.net/stocks/charts/GOOG/google/eps-earnings-per-share-diluted
eps = 43.70

#DATA_ENTRY Highest PE Ratio from last 10 years
#https://www.macrotrends.net/stocks/charts/GOOG/google/pe-ratio
highestPeRatio = 58.26

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