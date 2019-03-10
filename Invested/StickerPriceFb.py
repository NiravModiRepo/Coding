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


############################################################
dataNetIncome.append(22111)
dataNetIncome.append(15920)
dataNetIncome.append(10188)
dataNetIncome.append(3669)
dataNetIncome.append(2925)
dataNetIncome.append(1491)
dataNetIncome.append(32)
dataNetIncome.append(668)
dataNetIncome.append(372)
dataNetIncome.append(122)
dataNetIncome.append(-56)

dataTotalEquity.append(84127)
dataTotalEquity.append(74347)
dataTotalEquity.append(59194)
dataTotalEquity.append(44218)
dataTotalEquity.append(36096)
dataTotalEquity.append(15470)
dataTotalEquity.append(11755)
dataTotalEquity.append(4899)
dataTotalEquity.append(2162)
dataTotalEquity.append(0)
dataTotalEquity.append(0)

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

dataNetSales.append(55838)
dataNetSales.append(40653)
dataNetSales.append(27638)
dataNetSales.append(17928)
dataNetSales.append(12466)
dataNetSales.append(7872)
dataNetSales.append(5089)
dataNetSales.append(3711)
dataNetSales.append(1974)
dataNetSales.append(777)
dataNetSales.append(272)

dataCashGenerated.append(29274)
dataCashGenerated.append(24216)
dataCashGenerated.append(16108)
dataCashGenerated.append(10320)
dataCashGenerated.append(7326)
dataCashGenerated.append(4222)
dataCashGenerated.append(1612)
dataCashGenerated.append(1549)
dataCashGenerated.append(698)
dataCashGenerated.append(155)
dataCashGenerated.append(0)

eps = 7.57

highestPeRatio = 90.64

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