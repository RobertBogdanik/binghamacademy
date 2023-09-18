##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

minutes = int(input("Enter the number of minutes: "))

years = minutes/60/24/365
days = (minutes-(math.floor(years)*60*24*365))/60/24
print(f"{minutes} minutes is approximately {math.floor(years)} years and {math.floor(days)} days")
