x1, y1, x2, y2, x3, y3 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

val = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

if val == 0:
    print(f"({x3}, {y3}) is on the line segment from ({x1}, {y1}) to ({x2}, {y2})")

else:
    print(f"({x3}, {y3}) is not on the line segment from ({x1}, {y1}) to ({x2}, {y2})")
