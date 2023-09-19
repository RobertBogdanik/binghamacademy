##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 13.5.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

filename = input("Enter a filename: ")
old_string = input("Enter the string to be replaced: ")
new_string = input("Enter the new string: ")

content = open(filename, 'r').read()
content = content.replace(old_string, new_string)

open(filename, 'w').write(content)
