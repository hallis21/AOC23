lines = [line.strip().split() for line in open("18").readlines()]


corners = [(0, 0)]
current = (0, 0)

dirs2 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
for line in lines:
    hex = line[2][2:-1]
    # Hex decode

    # dist = int(hex[:-1], 16)
    # dir_val = dirs2[int(hex[-1])]
    # dir = (dir_val[0] * dist, dir_val[1] * dist)

    dir = dirs[line[0]]
    l = int(line[1])
    dir = (dir[0] * l, dir[1] * l)

    current = (current[0] + dir[0], current[1] + dir[1])
    corners.append(current)


original_corners = corners.copy()

rectangles = []


def corners_inside(rectangle, corners):
    corners_in = []
    for corner in corners:
        if corner[0] >= rectangle[0][0] and corner[0] <= rectangle[1][0]:
            if corner[1] >= rectangle[0][1] and corner[1] <= rectangle[1][1]:
                corners_in.append(corner)
    return corners_in


def on_same_x(corner, corner2):
    return corner[0] == corner2[0]


def on_same_y(corner, corner2):
    return corner[1] == corner2[1]


while len(corners) > 5:
    corners = sorted(corners, key=lambda x: (x[1], x[0]))
    cur_pair = corners[:2]
    corners = corners[2:]

    # If the index of the pair is after each other, add a rectangle
    diff = abs(original_corners.index(cur_pair[1]) - original_corners.index(cur_pair[0]))
    if diff == 1:
        rectangles.append((cur_pair[0], cur_pair[1]))
        continue
    

    first_stop_corner = None
    # Find all corners that have x inside the current pair x values
    min_x = min(cur_pair[0][0], cur_pair[1][0])
    max_x = max(cur_pair[0][0], cur_pair[1][0])
    corners_in_range = sorted(
        [corner for corner in corners if corner[0] >= min_x and corner[0] <= max_x],
        key=lambda x: (x[1], x[0]),
    )
    first_stop_corner = corners_in_range[0]

    rectangles.append((cur_pair[0], (cur_pair[1][0], first_stop_corner[1])))

    new_corners = []

    corners_inside_rect = corners_inside(
        (cur_pair[0], (cur_pair[1][0], first_stop_corner[1])), corners
    )

    # For cur_pair, if no corers inside on same x, add a corner at cur_pairy+1
    same_p1 = [
        corner for corner in corners_inside_rect if on_same_x(corner, cur_pair[0])
    ]
    if same_p1 == []:
        new_corners.append((cur_pair[0][0], first_stop_corner[1] + 1))
    else:
        for corner in same_p1:
            corners.remove(corner)
            corners_inside_rect.remove(corner)

    same_p2 = [
        corner for corner in corners_inside_rect if on_same_x(corner, cur_pair[1])
    ]
    if same_p2 == []:
        new_corners.append((cur_pair[1][0], first_stop_corner[1] + 1))
    else:
        for corner in same_p2:
            corners.remove(corner)
            corners_inside_rect.remove(corner)

    for corner in corners_inside_rect:
        corners.remove(corner)
        # y+1
        new_corners.append( (corner[0], corner[1] + 1) )

    corners += new_corners
    print(new_corners)



print(corners)

rectangles.append((corners[0], corners[1]))

print(rectangles)

# For each rectangle, find the area
# Add all areas together
# Add the perimeter of the rectangles together as well
area = 0
perimeter = 0
for rectangle in rectangles:
    area += (rectangle[1][0] - rectangle[0][0]) * (rectangle[1][1] - rectangle[0][1])
    perimeter += 2 * (rectangle[1][0] - rectangle[0][0]) + 2 * (
        rectangle[1][1] - rectangle[0][1]
    )
print(area + perimeter)

# Print a grid where the rectangles are drawn with #

grid = [["." for i in range(10)] for j in range(10)]
for rectangle in rectangles:
    for x in range(rectangle[0][0], rectangle[1][0]):
        for y in range(rectangle[0][1], rectangle[1][1]):
            grid[y][x] = "#"

# With idx 2digt
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        print(cell, end="")
    print()
