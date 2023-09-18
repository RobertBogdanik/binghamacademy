import turtle

x1, y1, x2, y2, x3, y3 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

def drawPoint(x, y, c=2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"({x}, {y})")
    turtle.begin_fill()
    turtle.circle(c)
    turtle.end_fill()


drawPoint(x1, y1)
drawPoint(x2, y2)
drawPoint(x3, y3, 5)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
turtle.penup()
turtle.goto(x3, y3)

val = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

if val<0:
    turtle.write("p2 is on the right side of the line")
elif val == 0:
    turtle.write("p2 is on the same line")
else:
    turtle.write("p2 is on the left side of the line")

turtle.mainloop()