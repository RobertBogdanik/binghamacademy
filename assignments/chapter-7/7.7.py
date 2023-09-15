##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

class LinearEquation:
    __a: any
    __b: any
    __c: any
    __d: any
    __e: any
    __f: any

    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def isSolvable(self):
        return (self.__a * self.__d - self.__b * self.__c) == 0

    def getX(self):
        if (self.__a * self.__d - self.__b * self.__c) == 0:
            return "The equation has no solution."
        top = self.__e * self.__d - self.__b * self.__f
        bottom = self.__a * self.__d - self.__b * self.__c
        return top/bottom

    def getY(self):
        if (self.__a * self.__d - self.__b * self.__c) == 0:
            return "The equation has no solution."
        top = self.__a * self.__f - self.__e * self.__c
        bottom = self.__a * self.__d - self.__b * self.__c
        return top/bottom

o = LinearEquation()
print(o.get_a())