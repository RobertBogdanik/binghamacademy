ISBN = input("Enter the first 12 digits of an ISBN-13: ")

sum = 0
for i in range(1, 13):
    if i % 2 == 0:
        sum += int(ISBN[i - 1]) * 3
    else:
        sum += int(ISBN[i - 1])

checksum = 10 - sum % 10

if checksum == 10:
    print(f"The ISBN-13 number is {ISBN}0")
else:
    print(f"The ISBN-13 number is {ISBN}{checksum}")
