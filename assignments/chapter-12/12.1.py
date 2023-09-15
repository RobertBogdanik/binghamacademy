##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

class GeometricObject:
    def __init__(self, color, filled):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return f"Color: {self.__color}, Filled: {self.__filled}"


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="white", filled=False):
        super().__init__(color, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)) ** 0.5
        return area

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"Triangle: side1 = {self.__side1}, side2 = {self.__side2}, side3 = {self.__side3}"


# Test program
side1 = float(input("Enter side 1 of the triangle: "))
side2 = float(input("Enter side 2 of the triangle: "))
side3 = float(input("Enter side 3 of the triangle: "))
color = input("Enter the color of the triangle: ")
filled = bool(int(input("Enter 1 for filled, 0 for not filled: ")))

triangle = Triangle(side1, side2, side3, color, filled)

print("Triangle properties:")
print(triangle)
print(f"Area: {triangle.getArea()}")
print(f"Perimeter: {triangle.getPerimeter()}")
print(f"Color: {triangle.getColor()}")
print(f"Filled: {triangle.isFilled()}")