##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 2.12.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

a = 1
b = 2

print(f"a\tb\ta ** b")
for x in range(5):
    print(f"{a}\t{b}\t{a**b}")
    a += 1
    b += 1
