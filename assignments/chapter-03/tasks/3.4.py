##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.4.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

s = eval(input("Enter the side: "))

area = (5*s**2)/(4*math.tan(math.pi/5))

print(f"The area of the pentagon is {area}")
