class Points:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distance(self, point):
        return ((self.__x - point.getX()) ** 2 + (self.__y - point.getY()) ** 2) ** 0.5
    def isNearBy(self, point):
        return self.distance(point) < 5
    def __str__(self):
        return f"({self.__x}, {self.__y})"

x1, y1, x2, y2 = eval(input("Enter x1, y1, x2, y2: "))
point1 = Points(x1, y1)
point2 = Points(x2, y2)
print(f"The distance between the two points is {point1.distance(point2)}")
if point1.isNearBy(point2):
    print(f"The two points are near each other")
else:
    print(f"The two points are not near each other")
