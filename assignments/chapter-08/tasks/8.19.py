class Rectangle2D:
    __x: float
    __y: float

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def containsPoint(self, x, y):
        if x > self.__x + self.__width / 2 or x < self.__x - self.__width / 2:
            return False
        if y > self.__y + self.__height / 2 or y < self.__y - self.__height / 2:
            return False
        return True

    def contains(self, rectangle):
        if self.containsPoint(rectangle.getX() + rectangle.__width / 2, rectangle.getY() + rectangle.__height / 2) and self.containsPoint(rectangle.getX() - rectangle.__width / 2, rectangle.getY() - rectangle.__height / 2):
            return True
        return False

    def overlaps(self, rectangle):
        if self.containsPoint(rectangle.getX() + rectangle.__width / 2, rectangle.getY() + rectangle.__height / 2) or self.containsPoint(rectangle.getX() - rectangle.__width / 2, rectangle.getY() - rectangle.__height / 2):
            return True
        return False

    def __contains__(self, item):
        return self.contains(item)

    def __lt__(self, other):
        return self.getArea() < other.getArea()

    def __le__(self, other):
        return self.getArea() <= other.getArea()

    def __eq__(self, other):
        return self.getArea() == other.getArea()

    def __ne__(self, other):
        return self.getArea() != other.getArea()

    def __gt__(self, other):
        return self.getArea() > other.getArea()

    def __ge__(self, other):
        return self.getArea() >= other.getArea()

    def __cmp__(self, other):
        return self.getArea() - other.getArea()

x1, y1, width1, height1 = eval(input("Enter x1, y1, width1, height1: "))
x2, y2, width2, height2 = eval(input("Enter x2, y2, width2, height2: "))

r1 = Rectangle2D(x1, y1, width1, height1)
r2 = Rectangle2D(x2, y2, width2, height2)

print(f"Area for r1 is {r1.getArea()}")
print(f"Perimeter for r1 is {r1.getPerimeter()}")
print(f"Area for r2 is {r2.getArea()}")
print(f"Perimeter for r2 is {r2.getPerimeter()}")
print(f"r1 contains the center of r2? {r1.containsPoint(r2.getX(), r2.getY())}")
print(f"r1 contains r2? {r1.contains(r2)}")
print(f"r1 overlaps r2? {r1.overlaps(r2)}")
