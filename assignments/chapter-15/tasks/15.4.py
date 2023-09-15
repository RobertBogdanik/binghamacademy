##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.4.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def m(i):
    if i == 1:
        return 1
    else:
        return m(i - 1) + 1 / i

for i in range(1, 11):
    result = m(i)
    print(f"m({i}) = {result:.5f}")
    