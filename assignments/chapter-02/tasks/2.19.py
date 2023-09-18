##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

investmentAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number of years: "))
monthlyInterestRate = annualInterestRate / 1200
numberOfMonths = numberOfYears * 12
futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths
print(f"Accumulated value is {round(futureInvestmentValue, 2)}")
