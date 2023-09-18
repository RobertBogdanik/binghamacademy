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
    turtle.circle(25)


draw(-25, 25)
draw(25, 25)
draw(-25, -25)
draw(25, -25)
