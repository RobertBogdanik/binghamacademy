##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 08/??/2023                   #
# Filename: 1.4.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

print(f"a\ta^2\ta^3")

for number in range(1, 5):
    print(f"{number}\t"
          f"{pow(number, 2)}\t"
          f"{pow(number, 3)}")

    