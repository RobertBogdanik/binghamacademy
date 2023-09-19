##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 13.8.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

filename = input("Enter a filename: ")
string_to_remove = input("Enter the string to be removed: ")

content = open(filename, 'r').read()
content = content.replace(string_to_remove, '')

open(filename, 'w').write(content)
