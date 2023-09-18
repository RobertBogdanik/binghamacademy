def sumDigits(n):
    if n == 0:
        return 0
    return n % 10 + sumDigits(n // 10)

userDigit = eval(input("Enter an integer: "))
print(f"The sum of digits of {userDigit} is {sumDigits(userDigit)}")
