import  math

number = 1
sum = 0
while number < 625:
    sum += 1/(math.sqrt(number) + math.sqrt(number + 1))
    number += 1

print(sum)