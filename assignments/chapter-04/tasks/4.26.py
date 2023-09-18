number = eval(input("Enter a three-digit integer: "))

if number // 100 == number % 10:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
