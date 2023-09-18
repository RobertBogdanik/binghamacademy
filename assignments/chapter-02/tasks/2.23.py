##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.23.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################
 
import turtle

radius = eval(input("Enter the radius: "))
turtle.penup()
turtle.goto(radius, -radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, -radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, radius)
turtle.pendown()
turtle.circle(radius)

turtle.mainloop()
