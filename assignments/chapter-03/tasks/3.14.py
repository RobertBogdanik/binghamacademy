# (Turtle: draw the Olympic symbol ) Write a program that prompts the user to
# enter the radius of the rings and draws an Olympic symbol of five rings of the
# same size with the colors blue, black, red, yellow, and green, as shown in
# Figure 3.5c.

import turtle

radius = eval(input("Enter the radius of the rings: "))

turt = turtle.Turtle()
turt.hideturtle()
turt.width(5)


def print_circle(color, x, y):
    turt.color(color)
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.circle(radius)


print_circle("blue", (-110/45)*radius, (-25/45)*radius)
print_circle("black", 0, (-25/45)*radius)
print_circle("red", (110/45)*radius, (-25/45)*radius)
print_circle("yellow", (-55/45)*radius, (-75/45)*radius)
print_circle("green", (55/45)*radius, (-75/45)*radius)


turtle.mainloop()
