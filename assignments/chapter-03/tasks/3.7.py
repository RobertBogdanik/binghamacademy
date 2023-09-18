##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: ??/??/2023                   #
# Filename: 3.7.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

import time

tim = time.time()

print("The random uppercase letter is", chr(ord('A') + int(tim % 26)))
