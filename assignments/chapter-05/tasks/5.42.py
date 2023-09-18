import random

odd = 0
even = 0

for i in range(1000000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x > 0 and y > 0:
        if x > y:
            odd += 1
        else:
            even += 1
    elif x < 0 and y > 0:
        if -x > y:
            odd += 1
        else:
            even += 1
    elif x < 0 and y < 0:
        if -x > -y:
            odd += 1
        else:
            even += 1
    else:
        if x > -y:
            odd += 1
        else:
            even += 1

print("Odd:", odd)
print("Even:", even)
