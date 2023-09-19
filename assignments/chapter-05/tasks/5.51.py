##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 5.51.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import  turtle

turtle.penup()
turtle.goto(-200, 200)

for x in range(20):
    turtle.goto(-200, 200 - x * 20)
    turtle.pendown()
    turtle.goto(160, 200 - x * 20)
    turtle.penup()

for x in range(19):
    turtle.goto(-200 + x * 20, 200)
    turtle.pendown()
    turtle.goto(-200 + x * 20, -180)
    turtle.penup()

turtle.mainloop()
