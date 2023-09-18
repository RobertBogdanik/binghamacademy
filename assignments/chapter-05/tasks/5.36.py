# Programming Exercise 4.17 gives a program that
# plays the scissor, rock, paper game.


import random

options = ["scissor", "rock", "paper"]
computerPoints = 0
userPoints = 0

while True:
    computer = random.randint(0, 2)
    user = eval(input("scissor (0), rock (1), paper (2): "))
    if user < 0 or user > 2:
        print("Wrong input")
        continue

    print(f"\nC: {computerPoints}, U: {userPoints}")
    print(f"The computer is {options[computer]}. You are {options[user]}")

    if user == computer:
        print(f"The computer is {options[computer]}. You are {options[user]} too. It is a draw")
    elif user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
        print(f"The computer is {options[computer]}. You are {options[user]}. You lost")
        computerPoints += 1
    else:
        print(f"The computer is {options[computer]}. You are {options[user]}. You won")
        userPoints += 1

    if userPoints > 2 or computerPoints > 2:
        break

if userPoints > computerPoints:
    print("You won the game")
else:
    print("You lost the game")
