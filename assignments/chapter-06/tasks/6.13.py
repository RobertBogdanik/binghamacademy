def calculate(n):
    # print(f"{n/(n+1)}")
    if n == 1:
        return 1/2
    else:
        return n/(n+1) + calculate(n-1)

print(calculate(10))