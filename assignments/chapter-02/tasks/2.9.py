##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

ta = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
v = eval(input("Enter the wind speed in miles per hour: "))

twc = 35.74 + 0.6215*ta - 35.75*v**0.16 + 0.4275*ta*v**0.16

print(round(twc, 5))
