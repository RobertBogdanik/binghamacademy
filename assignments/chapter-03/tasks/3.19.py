##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.19.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

x1, y1 = eval(input("Enter the x1, y2: "))
x2, y2 = eval(input("Enter the x2, y2: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("(" + str(x1) + ", " + str(y1) + ")")

turtle.goto(x2, y2)
turtle.write("(" + str(x2) + ", " + str(y2) + ")")

turtle.mainloop()
