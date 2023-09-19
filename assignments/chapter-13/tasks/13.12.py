##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 13.12.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Modify the Triangle class in Exercise 12.1 to throw a
# TriangleError exception if the three given sides cannot form a triangle.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3
