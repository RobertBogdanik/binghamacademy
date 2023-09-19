##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 13.4.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

import os
import random

filename = input("Enter a filename: ")

if os.path.isfile(filename):
    print("The file already exists")
    exit()

with open(filename, 'w') as file:
    for x in range(100):
        file.write(f"{random.randint(1, 100)}\n")
