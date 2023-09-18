import random

coinRotation = random.randint(0, 1)

userGuess = eval(input("Enter your guess (0 for heads, 1 for tails): "))
if userGuess == coinRotation:
    print("Correct!")
else:
    print("Incorrect!")