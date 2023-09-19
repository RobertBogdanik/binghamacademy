import math

print("Degree\tSin\tCos")
for x in range(37):
    x *= 10
    rad = x * (math.pi / 180)
    print(f"{x}\t{round(math.sin(rad), 5)}\t{round(math.cos(rad), 5)}")
