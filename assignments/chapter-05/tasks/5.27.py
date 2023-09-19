i = 50000
n = 1
sign = True
val = 0
while n<i:
    val += ((-1)**(n+1))/(2*n-1)

    n+=1

print(4*val)