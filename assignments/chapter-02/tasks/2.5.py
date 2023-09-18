##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################
 
subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate: "))
count = gratuity * subtotal / 100
print(f"The gratuity is {round(count, 2)} and the total is {round(subtotal+count, 2)}")
