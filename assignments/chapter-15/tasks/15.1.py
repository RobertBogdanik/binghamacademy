##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def sumDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumDigits(n // 10)
    
def main():
    number = eval(input("Enter an integer: "))
    print("The sum of digits is", sumDigits(number))

main()
