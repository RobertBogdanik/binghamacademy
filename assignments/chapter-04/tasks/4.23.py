##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.23.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

x, y = eval(input("Enter a point with two coordinates: "))

if x > -5 and x < 5 and y >- 2.5 and y < 2.5:
    print(f"Point ({x}, {y}) is in the rectangle")
else:
    print(f"Point ({x}, {y}) is not in the rectangle")
