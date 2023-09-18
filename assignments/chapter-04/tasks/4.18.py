##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.18.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

dollarsToRMB = eval(input("Enter the exchange rate from dollars to RMB: "))
mode = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))
dollars = eval(input("Enter the dollar amount: "))

if mode == 0:
    print(f"${dollars} yuan is ${round(dollars*dollarsToRMB, 2)}")
elif mode == 1:
    print(f"${dollars} yuan is ${round(dollars/dollarsToRMB, 2)}")
else:
    print("Incorrect input")
