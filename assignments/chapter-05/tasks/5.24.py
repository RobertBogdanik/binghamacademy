##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.24.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

loanAmount = eval(input("Loan Amount: "))
numberOfYears = eval(input("Number of Years: "))
annualInterestRate = eval(input("Annual Interest Rate: "))

monthlyInterestRate = annualInterestRate / 1200
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

print("Monthly Payment: ", round(monthlyPayment, 2))
print("Total Payment: ", round(totalPayment, 2))

print("Payment# Interest Principal Balance")
balance = loanAmount
for i in range(1, numberOfYears * 12 + 1):
    interest = monthlyInterestRate * balance
    principal = monthlyPayment - interest
    balance = balance - principal
    print(i, "\t\t", round(interest, 2), "\t\t", round(principal, 2), "\t\t", round(balance, 2))
