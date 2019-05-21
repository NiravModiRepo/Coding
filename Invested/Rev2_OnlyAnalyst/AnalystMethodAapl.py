# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:22:45 2019

@author: Nirav Modi
"""

#DATA_ENTRY EPS
#https://www.macrotrends.net/stocks/charts/AAPL/apple/eps-earnings-per-share-diluted
eps = 11.91

#DATA_ENTRY
#https://finance.yahoo.com/quote/aapl/analysis/
#Grwoth Estimates - Next 5 Years (per annum)
windageRate = 13
windagePercent = windageRate/100

#DATA_ENTRY Highest PE Ratio from last 10 years
#https://www.macrotrends.net/stocks/charts/AAPL/apple/pe-ratio
highestPeRatio = 20.70

futureEps = eps

print("Windage PE Ratio: Min of 2xWindage Rate:", 2*windageRate, ", Highest PE Ratio: ", highestPeRatio)
windagePeRatio = min(2*windageRate, highestPeRatio)
print("\n")

################################################################################3

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