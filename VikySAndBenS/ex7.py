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

deg = 95.0

min = 25.0

sec = 5.0


decimaldeg = deg + min / 60 + sec/3600




print  str (deg) + ":" + str (min) + ":" + str (sec) +" = " + str (decimaldeg)