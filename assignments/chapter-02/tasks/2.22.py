##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 15.1.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

numberOfYears = eval(input("Enter the number of years: "))
currentPopulation = 312032486
secondsInYear = 365 * 24 * 60 * 60
birthsPerYear = secondsInYear // 7
deathsPerYear = secondsInYear // 13

for i in range(numberOfYears):
    currentPopulation += birthsPerYear - deathsPerYear
print(f"The population in {numberOfYears} years is {currentPopulation}")
