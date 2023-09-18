##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.16.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import time
print(f"The random uppercase letter is "
      f"{chr(ord('A') + int(time.time() % 26))}")

