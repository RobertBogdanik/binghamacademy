##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 7.5.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

import math

class RegularPolygon:
    __n: int
    __side: float
    __x: float = 0
    __y: float = 0

    def __init__(self, n=3, length=1, x_coordinate=0.0, y_coordinate=0.0):
        self.__n = n
        self.__side = length
        self.__x = x_coordinate
        self.__y = y_coordinate

    def get_n(self):
        return self.__n

    def get_side(self):
        return self.__side

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_n(self, n):
        self.__n = n

    def set_side(self, side):
        self.__side = side

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def getPerimeter(self):
        return self.__n*self.__side

    def getArea(self):
        return (self.__n*(self.__side**2))/(4*math.tan(math.pi/self.__n))


p1 = RegularPolygon()
p2 = RegularPolygon(6, 4)
p3 = RegularPolygon(10, 4, 5.6, 7.8)

print(f"p1\tarea:{p1.getArea()}\tperimeter:{p1.getPerimeter()}")
print(f"p2\tarea:{p2.getArea()}\tperimeter:{p2.getPerimeter()}")
print(f"p3\tarea:{p3.getArea()}\tperimeter:{p3.getPerimeter()}")