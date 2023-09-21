##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.20.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

for x in range(7):
    i = 0
    while i < x:
        i += 1
        print(i, end=" ")
    print("")

for x in range(7):
    i = 0
    while i < 6-x:
        i += 1
        print(i, end=" ")
    print("")

for x in range(7):
    i = 0
    while i < 6-x:
        print(" ", end=" ")
        i += 1
    i = 0
    while i < x:
        # print(" ")
        i += 1
        print(i, end=" ")
    print("")


for x in range(7):
    i = 0
    while i < 6-x:
        i += 1
        print(i, end=" ")
    print("")
