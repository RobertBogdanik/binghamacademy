##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

def isValid(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()
    if sides[0]+sides[1] > sides[2]:
        return True
    else:
        return False

def area(side1, side2, side3):
    p = (side1+side2+side3)/2
    return math.sqrt(p*(p-side1)*(p-side2)*(p-side3))

side1, side2, side3 = eval(input("Enter three sides in double: "))
if isValid(side1, side2, side3):
    print(f"The area of the triangle is {area(side1, side2, side3)}")
else:
    print("Input is invalid")
