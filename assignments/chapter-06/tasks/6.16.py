def numberOfDaysInAYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365

for i in range(2010, 2021):
    print(f"{i} has {numberOfDaysInAYear(i)} days")
