##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 13.3.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

filename = input("Enter a filename: ")

content = open(filename, 'r').read()

numbers = [int(x) for x in content.split()]

print(f"Sum: {sum(numbers)}")

avg = sum(numbers) / len(numbers)
print(f"Average: {avg}")
