import math

x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if distance <= abs(r1 - r2):
    print("circle2 is inside circle1")
elif distance <= r1 + r2:
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")
