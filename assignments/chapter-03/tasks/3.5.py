import math

s = eval(input("Enter the side: "))
n = eval(input("Enter the number of sides: "))

area = (n*s**2)/(4*math.tan(math.pi/n))

print(f"The area of the polygon is {area}")