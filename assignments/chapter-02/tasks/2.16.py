##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.16.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

v0, v1, t = eval(input("Enter v0, v1, and t: "))
a = (v1 - v0) / t
print(f"The average acceleration is {round(a, 4)}")
