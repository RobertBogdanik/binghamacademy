##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def reverse(elements):
    return elements[::-1]
# def reverse_list(lst):
#     start, end = 0, len(lst) - 1
#     while start < end:
#         lst[start], lst[end] = lst[end], lst[start]
#         start += 1
#         end -= 1
#     return lst

numbers = input("Enter numbers: ").split(",")
rev = reverse(numbers)

print(f"reversed: {[float(el) for el in rev]}")
