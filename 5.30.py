from calendar import monthrange

firstday = eval(input("Day: "))
year = eval(input("Year: "))
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

data = monthrange(2005, 1)
print(data)
move = firstday - data[0]

for x in range(1, 13):
    data = monthrange(2005, x)
    firstday += data[1]
    firstday %= 7
    print(f" 1, {year} is {weekdays[firstday]}")
