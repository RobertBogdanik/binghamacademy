import math


def calculate(radius):
    area = pow(radius, 3)*math.pi
    perimeter = 2*radius*math.pi
    print(area)
    print(perimeter)


calculate(5.5)
