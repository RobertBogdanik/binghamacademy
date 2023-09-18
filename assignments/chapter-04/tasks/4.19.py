##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.19.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

e1, e2, e3 = eval(input("Enter three edges: "))

if e1 + e2 > e3 and e1 + e3 > e2 and e2 + e3 > e1:
    print(f"The perimeter is {e1 + e2 + e3}")
else:
    print("The input is invalid")