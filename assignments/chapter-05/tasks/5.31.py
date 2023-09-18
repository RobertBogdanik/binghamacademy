year = eval(input("Enter a year: "))
firstday = eval(input("Enter the first day of the year: "))

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
            "October", "November", "December"]

for month in range(1, 13):
    print(f"\n\n{months[month-1]} {year}")
    print("-----------------------------")
    for day in range(7):
        print(weekdays[day], end=" ")
    print()

    for day in range(firstday):
        print("    ", end=" ")
    for day in range(1, 32):
        if day < 10:
            print(f" {day} ", end=" ")
        else:
            print(f"{day} ", end=" ")
        if (day + firstday) % 7 == 0:
            print()
    firstday += 31
    firstday %= 7
