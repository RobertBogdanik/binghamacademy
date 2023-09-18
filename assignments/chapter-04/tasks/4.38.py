import turtle

x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

def drawRect(x, y, w, h):
    turtle.penup()
    turtle.goto(x + w / 2, y + h / 2)
    turtle.pendown()
    turtle.goto(x - w / 2, y + h / 2)
    turtle.goto(x - w / 2, y - h / 2)
    turtle.goto(x + w / 2, y - h / 2)
    turtle.goto(x + w / 2, y + h / 2)


drawRect(x1, y1, w1, h1)
drawRect(x2, y2, w2, h2)
turtle.penup()
turtle.goto(0, 30)

if x2 + w2 / 2 <= x1 + w1 / 2 and x2 - w2 / 2 >= x1 - w1 / 2 and y2 + h2 / 2 <= y1 + h1 / 2 and y2 - h2 / 2 >= y1 - h1 / 2:
    turtle.write("r2 is inside r1")
elif x2 + w2 / 2 >= x1 + w1 / 2 or x2 - w2 / 2 <= x1 - w1 / 2 or y2 + h2 / 2 >= y1 + h1 / 2 or y2 - h2 / 2 <= y1 - h1 / 2:
    turtle.write("r2 overlaps r1")
else:
    turtle.write("r2 does not overlap r1")

turtle.mainloop()
