##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.15.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

side = eval(input("Enter the side: "))
area = (3*math.sqrt(3)*pow(side, 2))/2
print(f"The area of the hexagon is {round(area, 4)}")

