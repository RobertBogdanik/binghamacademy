import math

radius, length = eval(input("Enter the radius and length of a cylinder"))

area = radius * radius * math.pi
volume = area * length

print(f"The area is {round(area, 2)}\n"
      f"The volume is {round(volume, 2)}")
