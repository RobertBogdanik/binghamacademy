def getPentagonalNumber(n):
    return (n*(3*n-1))/2

number = 1
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{getPentagonalNumber(number):<10}", end="")
        number += 1
    print()
    