def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

for n in range(10001):
    if isPrime(n):
        print(n)