numbers = eval(input("Enter a number between 0 and 1000: "))


def add(number=0):
    if number < numbers:
        return number+add(number+1)
    else:
        return number


print(add())
