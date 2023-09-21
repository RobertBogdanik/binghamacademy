##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.19.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

number = int(input("Enter the number of lines: \n"))

for x in range(number+1):
    print("  " * (number - x), end="")
    for y in range(x, 0, -1):
        print(y, end=" ")
    for y in range(2, x + 1):
        print(y, end=" ")

    print("")
