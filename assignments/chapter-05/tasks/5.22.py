##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.22.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

count = 0
for number in range(2, 1001):
    isPrime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime:
        count += 1
        print(number, end=" ")
        if count % 8 == 0:
            print("")
