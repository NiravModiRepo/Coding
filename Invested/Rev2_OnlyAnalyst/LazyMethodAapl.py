# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:22:45 2019

@author: Nirav Modi
"""

#DATA_ENTRY EPS
#https://finance.yahoo.com/quote/aapl/
#EPS-TTM
eps = 11.91

#DATA_ENTRY
#https://finance.yahoo.com/quote/aapl/analysis/
#Growth Estimates - Next 5 Years (per annum)
windagePercent = 13
windageRatio = windagePercent/100

windagePeRatio = 2*windagePercent
print("\n")

################################################################################3

#Step One
for i in range(0,10):
    eps *= (1+windageRatio)
    #print("Year", i, "Price: ", futureEps)

print("\n")
    
print("Step One: Future EPS: ", eps)

#Step Two
future10YearSharePrice = eps * windagePeRatio
print("Step Two: Future 10 Year Share Price: ", future10YearSharePrice)

#Step Three
stickerPrice = future10YearSharePrice / 4
print("Step Three: Sticker Price: ", stickerPrice)

#Step Four
marginOfSafetyPrice = stickerPrice/2
print("Step Four: Margin Of Safety Price: ", marginOfSafetyPrice)