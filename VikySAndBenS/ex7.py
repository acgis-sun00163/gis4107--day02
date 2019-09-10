#-------------------------------------------------------------------------------
# Name:      Exercise 7
# Purpose:   Convert degrees minutes to decimal degrees
#            Decimal Degrees = degrees + (minutes/60) + (seconds/3600)
#            add 0 after number
# Author:      chengjiaqi sun
#
# Created:     10/09/2019
# Copyright:   (c) cheng 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

deg = 95

min = 25

sec = 5




decimaldeg = deg + min / 60.0 + sec/3600.0




print  str (deg) + ":" + str (min) + ":" + str (sec) +" = " + "%.8f" % decimaldeg