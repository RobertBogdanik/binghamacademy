##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.5.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def m(i):
    if i == 1:
        return 1/3
    else:
        return m(i-1) + i/(2*i+1)
    
def main():
    for i in range(1, 11):
        print(f"m({i}) = {m(i)}")

main()
