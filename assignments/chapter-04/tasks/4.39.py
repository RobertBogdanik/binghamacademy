import math
import turtle

x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius: "))


def drawCircle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)


drawCircle(x1, y1, r1)
drawCircle(x2, y2, r2)

turtle.penup()
turtle.goto(0, 30)

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if distance <= abs(r1 - r2):
    turtle.write("circle2 is inside circle1")
elif distance <= r1 + r2:
    turtle.write("circle2 overlaps circle1")
else:
    turtle.write("circle2 does not overlap circle1")

turtle.mainloop()
