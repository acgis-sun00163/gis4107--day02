#-------------------------------------------------------------------------------
# Name:      Exercise 5
# Purpose:   acres to edge length of a square in meters
#
# Author:      chengjiaqi Sun
#
# Created:     10/09/2019
# Copyright:   (c) cheng 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

ac = 2

sqaureM = ac * 4046.86

length = math.sqrt(sqaureM)

print "Edge length of " + str(ac) + " acres square is " + str(length) + " metres "