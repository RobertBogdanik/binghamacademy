##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

amount = eval(input("Enter the amount of water in kilograms: "))
initial = eval(input("Enter the initial temperature: "))
finalt = eval(input("Enter the final temperature:"))

Q = amount * ( finalt - initial ) * 4184

print(f"The energy needed is {Q}")


