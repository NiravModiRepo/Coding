# -*- coding: utf-8 -*-

"""

Created on Wed Jan 8, 2020



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

#https://www.macrotrends.net/stocks/charts/nvda/nvidia/net-income

dataNetIncome.append(4141)

dataNetIncome.append(3047)

dataNetIncome.append(1666)

dataNetIncome.append(614)

dataNetIncome.append(631)

dataNetIncome.append(440)

dataNetIncome.append(563)

dataNetIncome.append(581)

dataNetIncome.append(253)

dataNetIncome.append(-68)

dataNetIncome.append(-30)



#DATA_ENTRY Equity from Balance Sheet

#https://www.macrotrends.net/stocks/charts/AAPL/apple/total-share-holder-equity

dataTotalEquity.append(9342)

dataTotalEquity.append(7471)

dataTotalEquity.append(5762)

dataTotalEquity.append(4469)

dataTotalEquity.append(4418)

dataTotalEquity.append(4456)

dataTotalEquity.append(4828)

dataTotalEquity.append(4146)

dataTotalEquity.append(3181)

dataTotalEquity.append(2665)

dataTotalEquity.append(2395)



#DATA_ENTRY Dividends from Cash Flow Statement

#https://www.macrotrends.net/stocks/charts/NVDA/nvidia/common-stock-dividends-paid

dataDividends.append(-371)

dataDividends.append(-341)

dataDividends.append(-261)

dataDividends.append(-213)

dataDividends.append(-186)

dataDividends.append(-181)

dataDividends.append(-47)

dataDividends.append(0)

dataDividends.append(0)

dataDividends.append(0)

dataDividends.append(0)



#DATA_ENTRY Sales from Income Statement

#https://www.macrotrends.net/stocks/charts/AAPL/apple/revenue

dataNetSales.append(11719)

dataNetSales.append(9714)

dataNetSales.append(6910)

dataNetSales.append(5010)

dataNetSales.append(4682)

dataNetSales.append(4130)

dataNetSales.append(4280)

dataNetSales.append(3998)

dataNetSales.append(3543)

dataNetSales.append(3326)

dataNetSales.append(3425)



#DATA_ENTRY Operating Cash from Cash Flow Statement

#https://www.macrotrends.net/stocks/charts/NVDA/nvidia/cash-flow-from-operating-activities

dataCashGenerated.append(3743)

dataCashGenerated.append(3502)

dataCashGenerated.append(1672)

dataCashGenerated.append(1175)

dataCashGenerated.append(906)

dataCashGenerated.append(835)

dataCashGenerated.append(824)

dataCashGenerated.append(909)

dataCashGenerated.append(676)

dataCashGenerated.append(488)

dataCashGenerated.append(249)



#DATA_ENTRY EPS

#https://www.macrotrends.net/stocks/charts/NVDA/nvidia/eps-earnings-per-share-diluted

eps = 6.63



#DATA_ENTRY Highest PE Ratio from last 10 years

#https://www.macrotrends.net/stocks/charts/NVDA/nvidia/pe-ratio

highestPeRatio = 61.36



#DATA_ENTRY

#https://finance.yahoo.com/quote/aapl/analysis/

#Growth Estimates - Next 5 Years (per annum)

analystWindageRate = 12.50



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