##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.14.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import random

coinRotation = random.randint(0, 1)

userGuess = eval(input("Enter your guess (0 for heads, 1 for tails): "))
if userGuess == coinRotation:
    print("Correct!")
else:
    print("Incorrect!")