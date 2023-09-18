class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}, area={self.get_area()}, perimeter={self.get_perimeter()}"


rec1 = Rectangle(4, 40)
rec2 = Rectangle(3.5, 35.7)

print(rec1)
print(rec2)