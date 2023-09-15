##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
fedTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))
grossPay = hours * payRate

print(f"Employee Name: {name}")
print(f"Hours Worked: {hours}")
print(f"Pay Rate: ${payRate}")
print(f"Gross Pay: ${grossPay}")
print(f"Deductions:")
print(f"  Federal Withholding ({fedTax*100}%): ${grossPay*fedTax}")
print(f"  State Withholding ({stateTax*100}%): ${grossPay*stateTax}")
print(f"  Total Deduction: ${round(grossPay*(fedTax+stateTax), 2)}")
print(f"Net Pay: ${round(grossPay*(1-fedTax-stateTax), 2)}")
