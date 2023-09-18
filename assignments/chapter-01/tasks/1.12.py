##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import time
import turtle


def square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x+50, y)
    turtle.goto(x+50, y-50)
    turtle.goto(x, y-50)
    turtle.goto(x, y)

#
square(-50, 50)
square(0, 50)
square(-50, 0)
square(0, 0)


time.sleep(2)
turtle.clear()

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.goto(50, 0)

turtle.right(90)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(0, -50)


time.sleep(2)
turtle.left(90)
turtle.goto(0, 0)
turtle.clear()


turtle.right(120)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)

turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)

turtle.mainloop()
