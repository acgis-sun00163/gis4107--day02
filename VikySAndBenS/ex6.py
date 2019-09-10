#-------------------------------------------------------------------------------
# Name:      Exercise 6
# Purpose: numbers of bears
#
# Author:      chengjiaqi sun
#
# Created:     10/09/2019
# Copyright:   (c) cheng 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

BDens = 4

squareM = 10000000

squareKM = squareM/ 1000000

BearN = BDens * squareKM

print "when bear density is " + str(BDens) + " bears / sq. km and the area is " + str(squareM) + " sq.m, the probable number of bears is  " + str (BearN)