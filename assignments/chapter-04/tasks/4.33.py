##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.33.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

dec = eval(input("Enter a decimal value (0 to 15): "))
# dec to hex
if dec > 15 or dec < 0:
    print("Invalid input")
else:
    print(f"the hex value is {hex(dec)[2:]}")
