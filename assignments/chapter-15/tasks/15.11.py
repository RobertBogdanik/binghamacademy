##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def reverseDisplayHelper(s, high):
    if high == 0:
        return s[0]
    else:
        return s[high] + reverseDisplayHelper(s, high - 1)
    
def reverseDisplay(s):
    return reverseDisplayHelper(s, len(s) - 1)

userString = input("Enter string: ")
print(f"Reversed string: {reverseDisplay(str(userString))}")
