import math

# MISTAKE IN THE BOOK
# 52.044441367816255

s = eval(input("Enter the side: "))

area = (5*(s**2))/(4*math.tan(math.pi/5))

print(f"The area of the pentagon is {area}")
