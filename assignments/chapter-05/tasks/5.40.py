import random

heads = 0
tails = 0

for i in range(1000000):
    coin = random.randint(0, 1)
    if coin == 0:
        heads += 1
    else:
        tails += 1
        
print("Heads:", heads)
print("Tails:", tails)