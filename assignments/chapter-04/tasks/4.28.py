# Geometry: two rectangles) Write a program that prompts the user to enter the
# center x-, y-coordinates, width, and height of two rectangles and determines
# whether the second rectangle is inside the first or overlaps with the first, as shown
# in Figure 4.10. Test your program to cover all cases.

x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

if x2 + w2 / 2 <= x1 + w1 / 2 and x2 - w2 / 2 >= x1 - w1 / 2 and y2 + h2 / 2 <= y1 + h1 / 2 and y2 - h2 / 2 >= y1 - h1 / 2:
    print("r2 is inside r1")
elif x2 + w2 / 2 >= x1 + w1 / 2 or x2 - w2 / 2 <= x1 - w1 / 2 or y2 + h2 / 2 >= y1 + h1 / 2 or y2 - h2 / 2 <= y1 - h1 / 2:
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
