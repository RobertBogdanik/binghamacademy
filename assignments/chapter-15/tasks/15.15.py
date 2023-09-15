##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def countHelper(chars, high):
    if high == 0:
        if chars[0].isupper():
            return 1
        else:
            return 0
    else:
        if chars[high].isupper():
            return 1 + countHelper(chars, high - 1)
        else:
            return countHelper(chars, high - 1)

def count(chars):
    return countHelper(chars, len(chars) - 1)

userList = input("Enter list of characters: ")
print(f"Number of uppercase letters in {userList}: {count(userList)}")
