
def displayPattern(n):
    for i in range(1, n + 1):
        print("\t" * (n - i), end="\t")
        for j in range(i, 0, -1):
            print(j, end="\t")
        print()

userNumber = eval(input("Enter an integer: "))
displayPattern(userNumber)