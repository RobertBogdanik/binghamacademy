
def count(num):
    res = 0
    bottom = 1
    for x in range(num):
        res += 1/bottom
        bottom += 2
        res -= 1/bottom
        bottom += 2
    return 4*res


print(count(3))
print(count(4))
print(count(60000))
