import random

n1 = random.randint(0, 100)
n2 = random.randint(0, 100)

sum = eval(input(f"What is {n1} + {n2}? "))

if sum == n1 + n2:
    print("true")
else:
    print(f"false")
