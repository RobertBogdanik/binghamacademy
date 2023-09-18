##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.5.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

todayDay = eval(input("Enter today's day: "))
elapsedSinceToday = eval(input("Enter the number of days elapsed since today: "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"Today is {days[todayDay]} and the future day is {days[(todayDay + elapsedSinceToday) % 7]}")

