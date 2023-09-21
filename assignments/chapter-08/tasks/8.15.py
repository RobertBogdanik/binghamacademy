ISBN = input("Enter the first 9 digits of an ISBN-10: ")

sum = 0
for i in range(1, 10):
    sum += int(ISBN[i - 1]) * i

checksum = sum % 11

if checksum == 10:
    print(f"The ISBN-10 number is {ISBN}X")
else:
    print(f"The ISBN-10 number is {ISBN}{checksum}")

