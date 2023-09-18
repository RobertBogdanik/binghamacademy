##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.4.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

import random

n1 = random.randint(0, 100)
n2 = random.randint(0, 100)

sum = eval(input(f"What is {n1} + {n2}? "))

if sum == n1 + n2:
    print("true")
else:
    print(f"false")
