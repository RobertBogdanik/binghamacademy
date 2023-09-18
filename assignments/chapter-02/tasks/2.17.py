##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.17.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))
weight = weight * 0.45359237
height = height * 0.0254
bmi = weight / (height**2)
print(f"BMI is {round(bmi, 4)}")
