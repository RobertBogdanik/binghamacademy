import turtle


def draw(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(25)


draw(-25, 25)
draw(25, 25)
draw(-25, -25)
draw(25, -25)
