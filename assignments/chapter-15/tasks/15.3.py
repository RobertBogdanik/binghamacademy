##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.3.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)
    
def main():
    m, n = eval(input("Enter two integers: "))
    print(f"The greatest common divisor of {m} and {n} is {gcd(m, n)}")

main()
