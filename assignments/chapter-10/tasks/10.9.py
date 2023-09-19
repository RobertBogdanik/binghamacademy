##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

string = input("Enter numbers: ")
numbers = string.split()


def mean(x):
    xsum = sum([float(el) for el in x])
    return sum([float(el) for el in x]) / len(x)


def deviation(x):
    mea = mean(x)
    sum_square = sum((float(xi) - mea)**2 for xi in x)
    return math.sqrt(sum_square/(len(x)-1))


print(f"The mean is {mean(numbers):.2f}")
print(f"The standard deviation is {deviation(numbers):.5f}")
