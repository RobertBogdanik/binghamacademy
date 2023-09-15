##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def countHelper(chars, ch, high):
    if high == 0:
        if chars[0] == ch:
            return 1
        else:
            return 0
    else:
        if chars[high] == ch:
            return 1 + countHelper(chars, ch, high - 1)
        else:
            return countHelper(chars, ch, high - 1)
        
def count(chars, ch):
    return countHelper(chars, ch, len(chars) - 1)

userList = input("Enter list of characters: ")
userChar = input("Enter character: ")
print(f"Number of occurrences of {userChar} in {userList}: {count(userList, userChar)}")
