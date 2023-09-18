##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.11.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

final = eval(input("Enter final account value: "))
annual = eval(input("Enter annual interest rate in percent: "))
number = eval(input("Enter number of years: "))


result = final / (1 + (annual / 1200)) ** (number * 12)

print(f"Initial deposit value is {result}")
