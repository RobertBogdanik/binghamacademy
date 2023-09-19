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
# go to left top corner
for x in range(11):
    turtle.goto(-200, 200 - x * 50)
    i = 0
    text = ""
    while i < x:
        i += 1
        text += str(i)

    turtle.write(text, font=("Arial", 16, "normal"))

turtle.mainloop()
