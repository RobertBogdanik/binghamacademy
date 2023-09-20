##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 4.36.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle
import random

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.goto(100, -100)
turtle.goto(100, 100)
turtle.goto(-100, 100)
turtle.goto(-100, -100)

x = random.randint(-100, 100)
y = random.randint(-100, 100)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(3)
turtle.end_fill()

if (x ** 2 + y ** 2) ** 0.5 <= 100:
    turtle.penup()
    turtle.goto(-100, -120)
    turtle.pendown()
    turtle.write("The point is inside the circle")
else:
    turtle.penup()
    turtle.goto(-100, -120)
    turtle.pendown()
    turtle.write("The point is outside the circle")

turtle.mainloop()
