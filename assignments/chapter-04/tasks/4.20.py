##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.20.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

ta = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
v = eval(input("Enter the wind speed in miles per hour: "))

if ta < -58 or ta > 41 or v<2:
    print("whether the temperature and/or wind speed is invalid")
else:
    print("wind-chill temperature")

