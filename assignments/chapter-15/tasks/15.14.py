##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def countHelper(s, a, high):
    if high == 0:
        if s[0] == a:
            return 1
        else:
            return 0
    else:
        if s[high] == a:
            return 1 + countHelper(s, a, high - 1)
        else:
            return countHelper(s, a, high - 1)
        
def count(s, a):
    return countHelper(s, a, len(s) - 1)

userString = input("Enter string: ")
userChar = input("Enter character: ")
print(f"Number of occurrences of {userChar} in {userString} is {count(userString, userChar)}")
