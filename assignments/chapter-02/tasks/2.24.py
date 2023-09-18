##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle


def draw(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(30)
    turtle.forward(100)
    for x in range(5):
        turtle.left(60)
        turtle.forward(100)
    turtle.left(30)


draw(-1.73205080757*50-10, 0)
draw(1.73205080757*50+10, 0)
draw(-1.73205080757*50-10, -200)
draw(1.73205080757*50+10, -200)

turtle.mainloop()
