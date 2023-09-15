##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def findLargestNumber(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], findLargestNumber(list[1:]))
    
userList = eval(input("Enter list of integers: "))
print(f"Largest number: {findLargestNumber(userList)}")
