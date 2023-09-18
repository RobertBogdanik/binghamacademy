##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.16.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################
 
import turtle

turtle.Turtle()
turtle.showturtle()
turtle.right(60)

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.circle(50, steps=3)

turtle.left(60)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
for x in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
for x in range(5):
    turtle.forward(50)
    turtle.left(72)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
for x in range(6):
    turtle.forward(50)
    turtle.left(60)

turtle.penup()
turtle.goto(250, 0)
turtle.pendown()
for x in range(8):
    turtle.forward(40)
    turtle.left(45)

turtle.mainloop()

