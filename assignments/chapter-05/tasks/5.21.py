number = 1
base = 17
current = 1

while current <= base:
    for x in range((base-current)//2):
        print(" ", end="\t")
    i = 0
    prev = 1
    while i < current//2-1:
        i += 1
        print(prev, end="\t")
        prev *= 2
    i = 0
    while i < current//2:
        i += 1
        print(prev, end="\t")
        prev //= 2
    print("")
    current += 2
