##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

radius, length = eval(input("Enter the radius and length of a cylinder"))

area = radius * radius * math.pi
volume = area * length

print(f"The area is {round(area, 2)}\n"
      f"The volume is {round(volume, 2)}")
