import random

n1 = random.randint(0, 10)
n2 = random.randint(0, 10)
n3 = random.randint(0, 10)

sum = n1 + n2 + n3

usersum = eval(input(f"What is {n1} + {n2} + {n3}? "))
if usersum == sum:
    print("You are correct!")
else:
    print(f"Your answer is wrong.\n"
          f"{n1} + {n2} + {n3} is {sum}")
