##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 13.9.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

input_file = input("Enter a input filename: ")
out_file = input("Enter a output filename: ")

content = open(input_file, 'r').read()

out = ""
for char in content:
    out += chr(ord(char) - 5)

open(out_file, 'w').write(out)