##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.26.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle
import math

x, y = eval(input("Enter the center of the circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))
turtle.penup()
turtle.goto(x, y-radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write(radius**2*math.pi)
turtle.mainloop()