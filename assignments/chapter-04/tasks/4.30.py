##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.30.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

timezone = eval(input("Enter the time zone offset to GMT: "))

import time

currentTime = time.time()

totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = (totalHours + timezone) % 24

if currentHour > 12:
    currentHour -= 12
    print(f"The current time is {currentHour}:{currentMinute}:{currentSecond} PM")
else:
    print(f"The current time is {currentHour}:{currentMinute}:{currentSecond} AM")
