##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.21.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

from calendar import weekday

year = eval(input("Enter year: (e.g., 2008): "))
month = eval(input("Enter month: 1-12:"))
day = eval(input("Enter the day of the month: 1-31:"))

weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"Day of the week is {weekDays[weekday(year, month, day)]}")
