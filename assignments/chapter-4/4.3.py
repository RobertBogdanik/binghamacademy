##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

if a*d-b*c != 0:
    x = (e*d-b*f)/(a*d-b*c)
    y = (a*f-e*c)/(a*d-b*c)
    print(f"x is {x} and y is {y}")

else:
    print("The equation has no solution")
