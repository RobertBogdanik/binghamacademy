import turtle

class SierpinskiTriangle(turtle.Turtle):
    def __init__(self, recurationDepth=3):
        super().__init__()
        self.width = 600
        self.height = 600
        self.penup()
        self.goto(-self.width / 2, -self.height / 2)
        self.pendown()
        self.speed(0)
        self.hideturtle()
        self.displayTriangles(recurationDepth, self.width, self.height)
        turtle.done()

    def displayTriangles(self, order, width, height):
        if order == 0:
            self.drawPolygon(width, height)
        else:
            self.displayTriangles(order - 1, width / 2, height / 2)
            self.forward(width / 2)
            self.displayTriangles(order - 1, width / 2, height / 2)
            self.backward(width / 2)
            self.left(60)
            self.forward(width / 2)
            self.right(60)
            self.displayTriangles(order - 1, width / 2, height / 2)
            self.left(60)
            self.backward(width / 2)
            self.right(60)

    def drawPolygon(self, width, height):
        self.begin_fill()
        self.forward(width)
        self.left(120)
        self.forward(height)
        self.left(120)
        self.forward(width)
        self.left(120)
        self.end_fill()

SierpinskiTriangle(7)

