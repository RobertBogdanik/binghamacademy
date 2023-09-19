numbers = []
sum = 0
positive = 0
negative = 0

# for i in range(4):
while len(numbers) < 4:
    num = eval(input(f"Enter an integer, the input ends if it is 0: "))
    if num == 0:
        print("You didn't enter any number")
        continue

    numbers.append(num)
    sum += num
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print(f"The number of positives is {positive}")
print(f"The number of negatives is {negative}")
print(f"The total is {sum}")
print(f"The average is {sum/len(numbers)}")
