##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.22.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

x1, y1 = eval(input("Enter a point with two coordinates: "))

if math.sqrt(x1**2 + y1**2) <= 10:
    print(f"Point ({x1}, {y1}) is in the circle")
else:
    print(f"Point ({x1}, {y1}) is not in the circle")

