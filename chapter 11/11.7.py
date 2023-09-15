import math

def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def find_nearest_points(points):
    if len(points) < 2:
        return None, None, float('inf')

    min_distance = float('inf')
    nearest_point1 = None
    nearest_point2 = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_distance:
                min_distance = d
                nearest_point1 = points[i]
                nearest_point2 = points[j]

    return nearest_point1, nearest_point2, min_distance

points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1],
          [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
          [5.5, 4, -0.5]]

point1, point2, min_dist = find_nearest_points(points)

print("The two nearest points:")
print(point1)
print(point2)
print("The minimum distance is:", min_dist)