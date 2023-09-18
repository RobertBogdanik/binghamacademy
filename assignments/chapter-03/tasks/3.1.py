##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.1.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################
 
import math

length = eval(input("Enter the length from the center to a vertex: "))

s = 2 * length * math.sin(math.pi / 5)
area = (3*math.sqrt(3)/2) * (s**2)

print(f"The area of the pentagon is {round(area, 2)}")
