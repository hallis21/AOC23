grid = [[x for x in y.strip()] for y in open('21').readlines()]

plots = set()
rocks = []

start = None

# Extract the coordinates of all "#"s
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] in ".":
            plots.add((x, y))
        if grid[y][x] == "S":
            start = (x, y)
        if grid[y][x] == "#":
            rocks.append((x, y))




visited = set()
reachable = {start}

distance_from_start = {
    start: 0
}


# Part 1
if False:
    current_distance = 1
    # Bfs to all neighbouring coordinates, 
    while len(reachable) > 0:
        new_reachable = set()
        for coord in reachable:
            x, y = coord
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_coord = (x + dx, y + dy)
                if new_coord not in distance_from_start and new_coord in plots:
                    new_reachable.add(new_coord)
                    distance_from_start[new_coord] = current_distance
        reachable = new_reachable
        current_distance += 1
        

#Part 2



big_steps = 26501365
counter = 0

plots.add(start)


results = []

for steps in range(1,100000):
    new_reachable = set()
    for coord in reachable:
        x, y = coord
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_coord = (x + dx, y + dy)
            # Check if the new cord is in coords
            # Since it can be outside the grid
            # find the rest after dividing by the length of the grid
            if (new_coord[0]%len(grid), new_coord[1]%len(grid)) in plots:
                new_reachable.add(new_coord)
    reachable = new_reachable


    # Check if the current steps is aligned
    if steps % len(grid) == big_steps % len(grid):
        print(steps, len(reachable))
        counter += 1
        results.append(len(reachable))
        if counter == 3:
            break


# Quadratic regression on the three points
total_repeats = big_steps//len(grid)

a0 = results[0]
a1 = results[1]
a2 = results[2]

b0 = a0
b1 = a1-a0
b2 = a2-a1

# The formula for the number of reachable plots after n steps
def f(n):
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

print(f(total_repeats))


exit()
print()
# Draw the grid, with rocks as "#", plots as ".", and start as "S", and visited as "O"
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (x, y) in rocks:
            print("#", end="")
        elif (x, y) in reachable_in_steps:
            print("O", end="")
        elif (x, y) in plots:
            print(".", end="")
        elif (x, y) == start:
            print("S", end="")
        else:
            print(" ", end="")
    print()
               














# distances = {}

# # For each coordinate, find the distance to all other coordinates
# for i in range(len(coordinates)):
#     x1, y1 = coordinates[i]
#     distances[(i, i)] = {}
#     for j in range(len(coordinates)):
#         x2, y2 = coordinates[j]
#         if i != j:
#             distances[(i, i)][(j, j)] = abs(x1 - x2) + abs(y1 - y2)

# steps = 64
# reachable = []

# for dist in distances[start]:
#     if distances[start][dist] <= steps:
#         # print(distances[start][dist])
#         reachable.append(dist)
# print(len(reachable))