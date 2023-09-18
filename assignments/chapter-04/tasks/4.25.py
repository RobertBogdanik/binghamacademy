##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.25.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))

a = (y1 - y2) / (x1 - x2)
b = y1 - a * x1

c = (y3 - y4) / (x3 - x4)
d = y3 - c * x3

try:
    print(f"The intersecting point is at ({(d - b) / (a - c)}, {(a * d - b * c) / (a - c)})")
except ZeroDivisionError:
    print("The two lines are parallel")
