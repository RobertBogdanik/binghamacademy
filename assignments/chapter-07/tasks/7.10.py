##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 7.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import time

class Time:
    __hour: int
    __minute: int
    __second: int

    def __init__(self):
        self.__hour = time.localtime().tm_hour
        self.__minute = time.localtime().tm_min
        self.__second = time.localtime().tm_sec

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elapseTime):
        self.__hour = elapseTime // 3600 % 24
        self.__minute = (elapseTime % 3600) // 60
        self.__second = (elapseTime % 3600) % 60

    def __str__(self):
        return f"{self.getHour()}:{self.getMinute()}:{self.getSecond()}"


o = Time()
print(o)
o.setTime(int(input("Enter the elapsed time: \n")))
print(o)


