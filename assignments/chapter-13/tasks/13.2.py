##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 13.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

filename = input("Enter a filename: ")

content = open(filename, 'r').read()

characters = len(content)
words = len(content.split())
lines = len(content.split('\n'))

print(f"Characters: {characters}\n"
      f"Words: {words}\n"
      f"Lines: {lines}")
