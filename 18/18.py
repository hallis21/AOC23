

lines = [x.split() for x in open("18").readlines()]

print(lines)

corners = {(0,0)}
edges = {(0,0)}
last_edge = (0,0)
for l in lines:
    val = (1,0) if l[0] == "R" else (-1,0) if l[0] == "L" else (0,1) if l[0] == "U" else (0,-1)
    l[1] = int(l[1])
    corners.add((last_edge[0] + val[0]*l[1], last_edge[1] + val[1]*l[1]))
    for i in range(int(l[1])):
        edges.add((last_edge[0] + val[0], last_edge[1] + val[1]))
        last_edge = (last_edge[0] + val[0], last_edge[1] + val[1])



min_x = min(edges, key=lambda x: x[0])[0]
max_x = max(edges, key=lambda x: x[0])[0]
min_y = min(edges, key=lambda x: x[1])[1]
max_y = max(edges, key=lambda x: x[1])[1]


all_squares = set(edges)

print(corners)
# Start in min_x, min_y


lines = [line.strip().split() for line in open("18").readlines()]


corners = {(0, 0)}
current = (0, 0)

dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

for line in lines:
    dir = dirs[line[0]]
    # dir = (dir[0] * int(line[1]), dir[1] * int(line[1]))
    for i in range(int(line[1])):
        current = (current[0] + dir[0], current[1] + dir[1])
        corners.add(current)


# Normalize so all corners are positive
minx = min([x[0] for x in corners])
miny = min([x[1] for x in corners])

corners = [(x[0] - minx, x[1] - miny) for x in corners]

minx = min([x[0] for x in corners])
miny = min([x[1] for x in corners])

maxx = max([x[0] for x in corners])
maxy = max([x[1] for x in corners])


# The corners make a closed area in the grid with no holes

# Use BFS to fill the inside of the area with #
# Start at the corner with min x, y can be anything
grid = [["." for i in range(maxx + 1)] for j in range(maxy + 1)]
# draw the corners
for corner in corners:
    grid[corner[1]][corner[0]] = "#"

print(corners)
# Find a corner with min x and . on both sides
for c in corners:
    if c[0] == minx:
        # print(c)
        if grid[c[1]][c[0] - 1] == "." and grid[c[1]][c[0] + 1] == ".":
            ## Ofset to the right since we know that is the inside
            start = (c[0] + 1, c[1])
            break

# print(start)

queue = [start]

while len(queue) > 0:
    current = queue.pop()
    if grid[current[1]][current[0]] == ".":
        grid[current[1]][current[0]] = "#"
        for dir in dirs.values():
            queue.append((current[0] + dir[0], current[1] + dir[1]))


# print(corner)
# exit()

# Draw the grid
# Add lines between the corners
            
# Count the # in the grid
count = 0
for line in grid:
    count += line.count("#")
print(count)


with open("18out", "w") as f:
    for line in grid:
        f.write("".join(line) + "\n")
