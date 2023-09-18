def m(i):
    result = 0
    for x in range(1, i + 1):
        result += ((-1) ** (x + 1)) / (2 * x - 1)
    return 4 * result


print("i\t\tm(i)")
for i in range(1, 1001, 100):
    print(i, "\t\t", round(m(i), 4))
