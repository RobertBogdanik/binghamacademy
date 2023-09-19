##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 5.46.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

# ?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# dziwne to
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def mean(numbers):
    return sum(numbers) / len(numbers)


def standard_deviation(numbers):
    mean_value = mean(numbers)
    sum_of_squares = 0
    for number in numbers:
        sum_of_squares += (number - mean_value) ** 2
    return (sum_of_squares / (len(numbers) - 1)) ** 0.5

numbers = []
while True:
    number = eval(input())
    if numbers == 10:
        break
    numbers.append(numbers)

print(f"The mean is {mean(numbers)}")
print(f"The standard deviation is {standard_deviation(numbers)}")