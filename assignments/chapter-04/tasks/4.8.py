##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.8.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

a, b, c = eval(input("Enter a, b, c: "))
userList = [a, b, c]
userList.sort()

print(f"The sorted numbers are {userList[0]} {userList[1]} {userList[2]}")
