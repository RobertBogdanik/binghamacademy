##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 08/??/2023                   #
# Filename: 1.13.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.goto(50, 0)

turtle.right(90)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(0, -50)

turtle.mainloop()
