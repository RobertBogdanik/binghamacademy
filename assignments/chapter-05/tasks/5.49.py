##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 5.49.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

turtle.penup()
turtle.goto(-200, 200)
turtle.write("Multiplication Table", font=("Arial", 16, "normal"))
turtle.goto(-200, 180)
turtle.write("       1   2   3   4   5   6   7   8   9", font=("Arial", 16, "normal"))

turtle.goto(-200, 160)
turtle.write("-----------------------------------------", font=("Arial", 16, "normal"))

for x in range(1, 10):
    turtle.goto(-200, 160 - x * 20)
    text = str(x) + " |"
    for y in range(1, 10):
        if x * y< 10:
            text += "   " + str(x * y)
        else:
            text += " " + str(x * y)
    turtle.write(text, font=("Arial", 16, "normal"))
    turtle.penup()

turtle.mainloop()


