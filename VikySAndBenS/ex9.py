#-------------------------------------------------------------------------------
# Name:      Exercise 9
# Purpose:
# 1 mile/gallon (US) =	425.1437075 m/L
# 35 U.S. MPG = 14.88 Kilometers per Liter  1 mile = 1. 61 km
# Author:      chengjiaqi sun
#
# Created:     10/09/2019
# Copyright:   (c) cheng 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

km = 100

mipergal = 35

dollarL = 1.30

kml = mipergal/2.35215054

price = km/kml*dollarL


print str(km) +" km at " + str(mipergal) + " mi/gal and $%.2f" % dollarL + " per L will cost $%.2f in total" % price