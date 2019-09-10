#-------------------------------------------------------------------------------
# Name:      Exercise 8
# Purpose:   decimal degrees to DMS
#            Decimal Degrees = degrees + (minutes/60) + (seconds/3600)
# Author:      chengjiaqi sun
#
# Created:     10/09/2019
# Copyright:   (c) cheng 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

dd = 95.41805


deg = int (dd)

m = int((dd - deg) * 60)

s = ((dd-deg) * 60 - m) * 60


sec =  int (0.41865 * 3600)


print  str(dd) + " = " + str (deg) + ":" + str (m) + ":" + "% .2f" % s

