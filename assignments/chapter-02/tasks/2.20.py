##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.20.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

balance, annualInterestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))
interest = balance * (annualInterestRate / 1200)
print(f"The interest is {round(interest, 5)}")
