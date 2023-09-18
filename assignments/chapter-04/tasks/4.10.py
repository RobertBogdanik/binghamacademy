##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input(f"What is {number1} * {number2}? "))
if number1 * number2 == answer:
    print("You are correct!")
else:
    print(f"Your answer is wrong.\n"
          f"{number1} * {number2} is {number1 * number2}")