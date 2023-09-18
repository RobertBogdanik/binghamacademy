def isPerfectNumber(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    if divisors_sum == number:
        return True
    else:
        return False


for i in range(1, 10000):
    if isPerfectNumber(i):
        print(i)
