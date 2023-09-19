##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 5.47.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle
import random

turtle.penup()
turtle.goto(-60, 50)
turtle.pendown()
turtle.goto(60, 50)
turtle.goto(60, -50)
turtle.goto(-60, -50)
turtle.goto(-60, 50)

def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

for x in range(10):
    draw_point(random.randint(-60, 60), random.randint(-50, 50))

turtle.mainloop()
