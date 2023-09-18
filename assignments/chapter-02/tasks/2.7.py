import math

minutes = int(input("Enter the number of minutes: "))

years = minutes/60/24/365
days = (minutes-(math.floor(years)*60*24*365))/60/24
print(f"{minutes} minutes is approximately {math.floor(years)} years and {math.floor(days)} days")
