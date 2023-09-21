##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.18.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

number = int(input("Enter the number: \n"))

prime_numbers = []
for x in range(2, number + 1):
    is_prime = True
    for y in range(2, x):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(x)

for x in prime_numbers:
    while number % x == 0:
        print(x, end=" ")
        number //= x
