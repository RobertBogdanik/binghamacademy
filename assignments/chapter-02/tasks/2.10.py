##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

speed, acceleration = eval(input("Enter speed and acceleration: "))

length = (speed**2)/(2*acceleration)

print(f"The minimum runway length for this airplane is {round(length, 3)} meters")
