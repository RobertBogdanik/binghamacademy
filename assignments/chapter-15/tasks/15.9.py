##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def reverseDisplay(value):
    if len(value) == 1:
        return value
    else:
        return reverseDisplay(value[1:]) + value[0]
    
userString = input("Enter string: ")
print(f"Reversed string: {reverseDisplay(str(userString))}")
