kg = 1
pound = 20

print("Kilograms\tPounds\t|\tPounds\tKilograms")
for x in range(1, 101):
    print(f"{kg}\t{round(kg*2.2, 2)}\t|\t{pound}\t{round(pound/2.2, 2)}")
    kg += 2
    pound += 5
