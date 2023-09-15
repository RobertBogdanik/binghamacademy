##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

v0, v1, t = eval(input("Enter v0, v1, and t: "))
a = (v1 - v0) / t
print(f"The average acceleration is {round(a, 4)}")
