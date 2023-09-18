import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)

while digit1 == digit2:
    digit2 = random.randint(0, 9)

lottery = str(digit1) + str(digit2)
print(lottery)
guess = input("Enter your lottery pick (two digits): ")

if guess == lottery:
    print("Exact match: you win $10,000")
elif guess[1] == lottery[0] and guess[0] == lottery[1]:
    print("Match all digits: you win $3,000")
elif guess[0] == lottery[0] or guess[0] == lottery[1] or guess[1] == lottery[0] or guess[1] == lottery[1]:
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")

