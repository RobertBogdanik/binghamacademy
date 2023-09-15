import random

user = eval(input("scissor (0), rock (1), paper (2): "))
computer = random.randint(0, 2)

if user == computer:
    print("The computer is", computer, "You are", user, "too. It is a draw.")
elif user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
    print("The computer is", computer, "You are", user, "You lost.")
else:
    print("The computer is", computer, "You are", user, "You won.")
