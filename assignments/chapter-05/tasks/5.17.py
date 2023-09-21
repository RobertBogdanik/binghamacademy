##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.17.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

for x in range(33, 127):
    print(chr(x), end=" ")
    if x % 10 == 2:
        print("")
