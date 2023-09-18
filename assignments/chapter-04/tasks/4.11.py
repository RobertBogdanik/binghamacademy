##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.11.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

from calendar import monthrange

month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(f"{months[month-1]} {year} has {monthrange(year, month)[1]} days")
