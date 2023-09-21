# Write a program that computes the following summation
# series using the Rational class:

# 1/2 + 2/3 + 3/4 + ... + 98/99 + 99/100


class Rational:
    def __init__(self, length):
        self.__length = length

    def claculate(self):
        sum = 0
        for i in range(1, self.__length + 1):
            sum += i / (i + 1)
        return sum

    def __str__(self):
        return f"{self.claculate()}"

print(Rational(10))
