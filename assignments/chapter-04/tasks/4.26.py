##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.26.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

number = eval(input("Enter a three-digit integer: "))

if number // 100 == number % 10:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
