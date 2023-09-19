miles = 1
km = 20

print("Kilograms\tPounds\t|\tPounds\tKilograms")
for x in range(1, 11):
    print(f"{miles}\t{round(miles*1.609, 2)}\t|\t{km}\t{round(km/1.609, 2)}")
    miles += 1
    km += 5
