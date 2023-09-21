##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 5.54.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200, 0)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.goto(0, -200)
turtle.penup()
turtle.goto(-20, 20**2)
for x in range(-20, 20):
    turtle.pendown()
    turtle.goto(x*5, x**2)

turtle.mainloop()
