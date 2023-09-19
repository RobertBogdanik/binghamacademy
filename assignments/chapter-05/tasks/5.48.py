##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 5.48.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

# Write a program that draws 10 circles with centers (0, 0), as
# shown in Figure 5.3b.

import turtle

def draw_circle(radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)

for x in range(50, 150, 10):
    draw_circle(x)


turtle.mainloop()