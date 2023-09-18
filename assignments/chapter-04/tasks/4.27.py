x, y = eval(input("Enter a point's x- and y-coordinates: "))
x1 = 0
y1 = 100

x2 = 200
y2 = 0

a = (y1 - y2) / (x1 - x2)
b = y1 - a * x1

if y > a * x + b or y < 0:
    print(f"The point is not in the triangle")
else:
    print(f"The point is in the triangle")

