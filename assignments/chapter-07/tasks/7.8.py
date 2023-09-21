##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 7.8.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

import time


class StopWatch:
    __startTime: float = 0
    __endTime: float = 0

    def __init__(self):
        import time
        self.__startTime = time.time()

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return (self.__endTime - self.__startTime) * 1000

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def setStartTime(self, startTime):
        self.__startTime = startTime

    def setEndTime(self, endTime):
        self.__endTime = endTime

    def __str__(self):
        return (f"Start time: {self.__startTime}\n"
                f"End time: {self.getEndTime()}\n"
                f"Elapsed time: {self.getElapsedTime()}")

o = StopWatch()
o.start()
time.sleep(1)
o.stop()
print(o)
