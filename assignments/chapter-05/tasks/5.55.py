##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.55.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle


def draw_square(side):
    turtle.begin_fill()
    turtle.color("black")
    for x in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()


for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            turtle.penup()
            turtle.goto(x * 20, y * 20)
            turtle.pendown()
            draw_square(20)
# mak frame
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 160)
turtle.goto(160, 160)
turtle.goto(160, 0)
turtle.goto(0, 0)


turtle.mainloop()
