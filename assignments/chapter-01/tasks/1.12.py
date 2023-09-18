##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 08/??/2023                   #
# Filename: 1.12.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

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

turtle.mainloop()
