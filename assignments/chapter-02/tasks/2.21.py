##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.21.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

# get monthly saving amount
monthlySavingAmount = eval(input("Enter the monthly saving amount: "))

# create variable for monthly interest rate and account value
monthlyInterestRate = 0.05 / 12
accountValue = 0

# calculate for each month
for i in range(6):
    accountValue = (monthlySavingAmount + accountValue) * (1 + monthlyInterestRate)

# print result
print(f"After the sixth month, the account value is {round(accountValue, 2)}")
