##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def fib(n):
    f0 = 0
    f1 = 1
    for i in range(2, n + 1):
        currentFib = f0 + f1
        f0 = f1
        f1 = currentFib
    return currentFib

index = eval(input("Enter an index: "))
print(f"The Fibonacci number at index {index} is {fib(index)}")
