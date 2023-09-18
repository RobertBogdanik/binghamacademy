##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################


import math


def calculate(radius):
    area = pow(radius, 3)*math.pi
    perimeter = 2*radius*math.pi
    print(area)
    print(perimeter)


calculate(5.5)
