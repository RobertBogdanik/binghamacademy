call = 0


def fib(index):
    global call
    call += 1
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


index = int(eval(input("Enter an index for a Fibonacci number: ")))
result = fib(index)
print(f"The Fibonacci number at index {index} is {result}")

print(f"Function was called {call} times")