##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.12.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import turtle

len = eval(input("Enter an integer: "))

for x in range(5):
    turtle.right(180-36)
    turtle.forward(len)

turtle.mainloop()
