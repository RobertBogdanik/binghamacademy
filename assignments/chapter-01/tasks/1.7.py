##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 08/??/2023                   #
# Filename: 1.7.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

def count(num):
    res = 0
    bottom = 1
    for x in range(num):
        res += 1/bottom
        bottom += 2
        res -= 1/bottom
        bottom += 2
    return 4*res


print(count(3))
print(count(4))
print(count(60000))
