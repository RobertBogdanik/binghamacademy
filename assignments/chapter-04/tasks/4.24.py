##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 4.24.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

rank = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

suit = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

import random

r = random.randint(0, 12)
s = random.randint(0, 3)

print(f"The card you picked is the {rank[r]} of {suit[s]}")
