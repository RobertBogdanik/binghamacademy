##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

tuition = 10000.00

for x in range(1, 11):
    print(f"{x} -> {round(tuition, 2)}")
    tuition *= 1.05
