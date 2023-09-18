# (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
# number of years and displays the population after that many years. Here is a
# sample run of the program:
# Enter the number of years:
# The population in 5 years is 325932970

numberOfYears = eval(input("Enter the number of years: "))
currentPopulation = 312032486
secondsInYear = 365 * 24 * 60 * 60
birthsPerYear = secondsInYear // 7
deathsPerYear = secondsInYear // 13

for i in range(numberOfYears):
    currentPopulation += birthsPerYear - deathsPerYear
print(f"The population in {numberOfYears} years is {currentPopulation}")
