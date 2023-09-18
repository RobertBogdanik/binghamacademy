##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.37.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

x, y = eval(input("Enter a point's x- and y-coordinates: "))

turtle.penup()
turtle.goto(-50, 25)
turtle.pendown()
turtle.goto(50, 25)
turtle.goto(50, -25)
turtle.goto(-50, -25)
turtle.goto(-50, 25)
turtle.penup()

turtle.goto(x, y)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.goto(-50, -50)
if x > 50 or x < -50 or y > 25 or y < -25:
    turtle.write("The point is not in the rectangle")
else:
    turtle.write("The point is in the rectangle")

turtle.mainloop()