
def reverse(number):
    return int(str(number)[::-1])

userNumber = eval(input("Enter a number: "))
print(f"Reverse of {userNumber} is {reverse(userNumber)}")

