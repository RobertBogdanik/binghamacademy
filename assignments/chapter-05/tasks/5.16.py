##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.16.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

number1 = int(input("Enter the first number: \n"))
number2 = int(input("Enter the second number: \n"))
divisor = min(number1, number2)
while divisor > 1:
    if number1 % divisor == 0 and number2 % divisor == 0:
        break
    divisor -= 1
print("The greatest common divisor is", divisor)
