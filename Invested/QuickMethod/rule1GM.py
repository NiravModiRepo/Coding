# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 01:24:06 2019

@author: nam42589
"""
# *** LEMONADE STAND ***
current_eps = 20
current_pe = 22
growth = 16

# *** GM ***
current_eps = 8.53
current_pe = 12
growth = 6

# *** WHOLE FOODS ***
current_eps = 1.48
growth = 14
current_pe = 28

# *** AMZN ***
current_eps = 20.14
growth = 91
current_pe = 92.50

# *** APPL ***
current_eps = 12.12
growth = 13
current_pe = 16.76

# *** GOOG ***
current_eps = 43.70
growth = 17.60
current_pe = 28.29

# *** MSFT ***
current_eps = 4.31
growth = 14.52
current_pe = 28.25

# *** NFLX ***
current_eps = 2.68
growth = 48.14
current_pe = 132.37

# *** DIS ***
current_eps = 7.30
growth = 3.97
current_pe = 18.05

# *** RHT ***
current_eps = 2.33
growth = 17
current_pe = 78.35

# *** FB ***
current_eps = 7.57
growth = 16.43
current_pe = 23.62

# *** WIX ***
current_eps = -0.77
growth = 187.21
current_pe = 0

#years = 10
#marr = 15
#marrMultiplier = 1 + (marr/100)

growth_rate = 1+(growth/100)


current_value = current_eps * current_pe

future_eps = pow(growth_rate, 10) * current_eps
future_pe = current_pe
future_value = future_eps * future_pe

mos = future_value/8
