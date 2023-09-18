##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.6.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))


KILOGRAMS_PER_POUND = 0.45359237
weightInKilograms = weight * KILOGRAMS_PER_POUND
METERS_PER_INCH = 0.0254
heightInMeters = (feet * 12 + inches) * METERS_PER_INCH

BMI = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", format(BMI, ".6f"), "You are ", end="")
if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
