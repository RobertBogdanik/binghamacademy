
todayDay = eval(input("Enter today's day: "))
elapsedSinceToday = eval(input("Enter the number of days elapsed since today: "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"Today is {days[todayDay]} and the future day is {days[(todayDay + elapsedSinceToday) % 7]}")

