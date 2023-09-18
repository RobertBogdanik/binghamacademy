##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.15.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)

# Prompt user for answer
u1 = eval(input(f"Enter 1 digit: "))
u2 = eval(input(f"Enter 2 digit: "))
u3 = eval(input(f"Enter 3 digit: "))

numbers = [n1, n2, n3]
# Check the answer
if u1 == n1 and u2 == n2 and u3 == n3:
    print("You win $10,000")
elif u1 in numbers and u2 in numbers and u3 in numbers:
    print("You win $3,000")
elif u1 in numbers or u2 in numbers or u3 in numbers:
    print("You win $1,000")
