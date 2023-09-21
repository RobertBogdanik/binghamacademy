##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 7.9.py                           #
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

x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment: \n"))
x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment: \n"))

a = y1 - y2
b = x2 - x1
e = x2 * y1 - x1 * y2
c = y3 - y4
d = x4 - x3
f = x4 * y3 - x3 * y4

o = LinearEquation(a, b, c, d, e, f)

print("The intersecting point is: (", o.getX(), ",", o.getY(), ")")

