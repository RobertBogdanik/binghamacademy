##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.12.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

number = eval(input("Enter an integer: "))

# by10 = number % 10 == 0
by5or6 = number % 5 == 0 or number % 6 == 0
by5and6 = number % 5 == 0 and number % 6 == 0
by5or6butNOtBoth = by5or6 and not by5and6

print(f"Is {number} divisible by 5 and 6? {by5and6}")
print(f"Is {number} divisible by 5 or 6? {by5or6}")
print(f"Is {number} divisible by 5 or 6, but not both? {by5or6butNOtBoth}")

