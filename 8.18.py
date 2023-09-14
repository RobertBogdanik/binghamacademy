import math


class Circle2D:
    __x: float = 0
    __y: float = 0
    __radius: any = 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def __init__(self, x=0, y=0, radius=0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getArea(self):
        return math.pi * self.__radius ** 2

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def containsPoint(self, x, y):
        return math.sqrt((x - self.__x) ** 2 + (y - self.__y) ** 2) < self.__radius

    def contains(self, circle):
        x = circle.get_x()
        y = circle.get_y()
        rad = circle.get_radius()
        d = math.sqrt((x - self.__x) ** 2 + (y - self.__y) ** 2)
        return d + rad < self.__radius

    def overlaps(self, circle):
        x = circle.get_x()
        y = circle.get_y()
        rad = circle.get_radius()
        d = math.sqrt((x - self.__x) ** 2 + (y - self.__y) ** 2)
        return d + rad > self.__radius > d

    def __contains__(self, another):
        return self.overlaps(another)

    def compare(self, another):
        if self.__radius < another.get_radius():
            return 1
        elif self.__radius == another.get_radius():
            return 0
        else:
            return -1

    def __cmp__(self, another):
        return self.compare(another)

    def __lt__(self, other):
        return self.compare(other) == 1

    def __le__(self, other):
        return self.compare(other) == 1 or self.compare(other) == 0

    def __eq__(self, other):
        return self.compare(other) == 0

    def __ne__(self, other):
        return self.compare(other) != 0

    def __gt__(self, other):
        return self.compare(other) == -1

    def __ge__(self, other):
        return self.compare(other) == -1 or self.compare(other) == 0
