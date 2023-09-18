##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.34.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

hex = input("Enter a hex digit: ")

if hex.upper() in ("A", "B", "C", "D", "E", "F") or int(hex) < 10:
    print(f"The hex value is {int(hex, 16)}")
else:
    print("Invalid input")
