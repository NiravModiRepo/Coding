"""
Created on Tue Feb 12 21:48:25 2019

@author: Nirav Modi

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
#https://www.macrotrends.net/stocks/charts/AMZN/amazon/net-income
dataNetIncome.append(10073)
dataNetIncome.append(3033)
dataNetIncome.append(2371)
dataNetIncome.append(596)
dataNetIncome.append(-241)
dataNetIncome.append(274)
dataNetIncome.append(-39)
dataNetIncome.append(631)
dataNetIncome.append(1152)
dataNetIncome.append(902)
dataNetIncome.append(645)

#DATA_ENTRY Equity from Balance Sheet
#https://www.macrotrends.net/stocks/charts/AMZN/amazon/total-share-holder-equity
dataTotalEquity.append(43549)
dataTotalEquity.append(27709)
dataTotalEquity.append(19285)
dataTotalEquity.append(13384)
dataTotalEquity.append(10741)
dataTotalEquity.append(9746)
dataTotalEquity.append(8192)
dataTotalEquity.append(7757)
dataTotalEquity.append(6864)
dataTotalEquity.append(5257)
dataTotalEquity.append(2672)

#DATA_ENTRY Dividends from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/AMZN/amazon/common-stock-dividends-paid
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
#https://www.macrotrends.net/stocks/charts/AMZN/amazon/revenue
dataNetSales.append(232887)
dataNetSales.append(177866)
dataNetSales.append(135987)
dataNetSales.append(107006)
dataNetSales.append(88988)
dataNetSales.append(74452)
dataNetSales.append(61093)
dataNetSales.append(48077)
dataNetSales.append(34204)
dataNetSales.append(24509)
dataNetSales.append(19166)

#DATA_ENTRY Operating Cash from Cash Flow Statement
#https://www.macrotrends.net/stocks/charts/AMZN/amazon/cash-flow-from-operating-activities
dataCashGenerated.append(30723)
dataCashGenerated.append(18365)
dataCashGenerated.append(17203)
dataCashGenerated.append(12039)
dataCashGenerated.append(6842)
dataCashGenerated.append(5475)
dataCashGenerated.append(4180)
dataCashGenerated.append(3903)
dataCashGenerated.append(3495)
dataCashGenerated.append(3293)
dataCashGenerated.append(1967)

#DATA_ENTRY EPS
#https://www.macrotrends.net/stocks/charts/AMZN/amazon/eps-earnings-per-share-diluted
eps = 20.14

#DATA_ENTRY Highest PE Ratio from last 10 years
#https://www.macrotrends.net/stocks/charts/AMZN/amazon/pe-ratio
highestPeRatio = 1116.57
#first highest 3633.14 
#second highest 1116.57

#DATA_ENTRY
#https://finance.yahoo.com/quote/amzn/analysis/
#Grwoth Estimates - Next 5 Years (per annum)
analystWindageRate = 43.81

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
    #print("Year", i, "Price: ", futureEps)

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