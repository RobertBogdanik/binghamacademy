##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.5.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

s = eval(input("Enter the side: "))
n = eval(input("Enter the number of sides: "))

area = (n*s**2)/(4*math.tan(math.pi/n))

print(f"The area of the polygon is {area}")