##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def countUppercaseHelper(s, high):
    if high == 0:
        if s[0].isupper():
            return 1
        else:
            return 0
    else:
        if s[high].isupper():
            return 1 + countUppercaseHelper(s, high - 1)
        else:
            return countUppercaseHelper(s, high - 1)

def countUppercase(s):
    return countUppercaseHelper(s, len(s) - 1)

userString = input("Enter string: ")
print(f"Number of uppercase letters in {userString}: {countUppercase(userString)}")

