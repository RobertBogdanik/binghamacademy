##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.18.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

x1, y1 = eval(input("Enter the x1, y2: "))
x2, y2 = eval(input("Enter the x2, y2: "))
x3, y3 = eval(input("Enter the x3, y3: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1 (" + str(x1) + ", " + str(y1) + ")")

turtle.goto(x2, y2)
turtle.write("p2 (" + str(x2) + ", " + str(y2) + ")")

turtle.goto(x3, y3)
turtle.write("p3 (" + str(x3) + ", " + str(y3) + ")")

turtle.goto(x1, y1)

turtle.mainloop()
