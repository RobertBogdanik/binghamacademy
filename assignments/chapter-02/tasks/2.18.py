##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.18.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import time

offset = eval(input("Enter the time zone offset to GMT: "))
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = (totalHours + offset) % 24
print(f"The current time is {currentHour}:{currentMinute}:{currentSecond}")
