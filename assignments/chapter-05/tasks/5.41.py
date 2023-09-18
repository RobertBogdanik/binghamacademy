max = 0
count = 0

while True:
    num = eval(input("Enter an integer (0 to end): "))
    if num == 0:
        break

    if num > max:
        max = num
        count = 1
    elif num == max:
        count += 1

print(f"The largest number is {max}")
print(f"The occurrence count of the largest number is {count}")
