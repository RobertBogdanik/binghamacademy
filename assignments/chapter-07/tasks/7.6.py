##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 7.6.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!! NOT FINISHED !!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!


import math


class QuadraticEquation:
    def __init(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def getDiscriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0

        if self.getDiscriminant() == 0:
            return "The equation has no roots."

        return (-self.__b + math.sqrt(self.getDiscriminant())) / (2 * self.__a)

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0

        return (-self.__b - math.sqrt(self.getDiscriminant())) / (2 * self.__a)


