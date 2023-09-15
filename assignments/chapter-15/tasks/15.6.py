##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.6.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def m(i):
    if i == 1:
        return 1/2
    else:
        return m(i-1) + i/(i+1)
    
def main():
    i = eval(input("Enter an integer: "))
    print(f"m({i}) = {m(i)}")
