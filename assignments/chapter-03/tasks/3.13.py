##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.13.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

turtle.penup()
turtle.goto(40, -69.28)

turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80, 0)
turtle.goto(40, -69.28)
turtle.end_fill()


turtle.goto(-40, -20)
turtle.color("white")
turtle.write("STOP", font=("Arial", 25, "normal"))
turtle.end_fill()
turtle.mainloop()
