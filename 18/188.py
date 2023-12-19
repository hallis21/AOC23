def polygon_area(coordinates):
    n = len(coordinates)
    area = 0.0

    for i in range(n - 1):
        area += (
            coordinates[i][0] * coordinates[i + 1][1]
            - coordinates[i + 1][0] * coordinates[i][1]
        )

    area += (
        coordinates[n - 1][0] * coordinates[0][1]
        - coordinates[0][0] * coordinates[n - 1][1]
    )

    area = abs(area) / 2.0
    return area


lines = [line.strip().split() for line in open("18").readlines()]


corners = [(0, 0)]
current = (0, 0)
circumference = 0
dirs2 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
for line in lines:
    hex = line[2][2:-1]
    # Hex decode

    dist = int(hex[:-1], 16)
    dir_val = dirs2[int(hex[-1])]
    dir = (dir_val[0] * dist, dir_val[1] * dist)

    # dir = dirs[line[0]]
    # l = int(line[1])
    # dir = (dir[0] * l, dir[1] * l)

    current = (current[0] + dir[0], current[1] + dir[1])
    circumference += dist
    corners.append(current)


def polygonArea(X, Y, n):
    # Initialize area
    area = 0.0

    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0, n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i  # j is previous vertex to i

    # Return absolute value
    return int(abs(area / 2.0))


X = [x[0] for x in corners]
Y = [x[1] for x in corners]
n = len(corners)
print(polygonArea(X, Y, n))

# Example usage:
# polygon_coordinates = [(0, 0), (0, 5), (3, 5), (3, 2), (5, 2), (5, 0)]
area = polygon_area(corners[:-1])
print("Area of the polygon:", int(area + (circumference / 2) + 1))
