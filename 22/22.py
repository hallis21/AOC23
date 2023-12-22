lines = [line.strip().split("~") for line in open('22')]

grid = []

max_x = 0
max_y = 0
max_z = 0
# min is 0

i = 0
for coord in lines:
    c = [cc.split(",") for cc in coord]
    # ((c[0][0], c[0][1] c[0][2]), (c[1][0], c[1][1], c[1][2])
    grid.append(((int(c[0][0]), int(c[0][1]), int(c[0][2])), (int(c[1][0]), int(c[1][1]), int(c[1][2]))))
    max_x = max(max_x, int(c[0][0]), int(c[1][0]))
    max_y = max(max_y, int(c[0][1]), int(c[1][1]))
    max_z = max(max_z, int(c[0][2]), int(c[1][2]))
    i += 1

# X,y are the horizontal plane
# Z is the vertical plane

# Order the grid by the min z value in the pair
# Lowest z first'
sorted_grid = grid.copy()
sorted_grid.sort(key=lambda x: min(x[0][2], x[1][2]))

# print(grid)

# Represents the min heigh possible at each point
# the -1 represents the index of the coord in the grid
stacks = [[(0, -1) for x in range(max_y+1)] for i in range(max_x+1)]
stack_ordered = set()
brick_heights = [1 for x in range(len(grid))]

# For each point in the grid
# Find the x,y coordinates that it covers

for i, coord in enumerate(sorted_grid):
    stack_coords = set()
    

    # For each x,y coordinate that it covers
    min_height = min(coord[0][2], coord[1][2])
    height = (max(coord[0][2], coord[1][2]) - min_height)+1
    max_z_brick = min_height + height

    

    min_stack_height = -1

    for x in range(coord[0][0], coord[1][0]+1):
        for y in range(coord[0][1], coord[1][1]+1):
            # For each x,y coordinate that it covers
            # Set the min possibly stack height to be the max of the current min height and the height of the current coord
            stack_coords.add((x,y))
            min_stack_height = max(min_stack_height, stacks[x][y][0])

    # if i == len(sorted_grid)-1:
        # print(height, max_z_brick, min_stack_height)
    for x,y in stack_coords:
        # Set all cords to min_stack_height + height
        new_height = min_stack_height + height
        stacks[x][y] = (new_height, grid.index(coord))
        stack_ordered.add((x,y, new_height, grid.index(coord)))
        brick_heights[grid.index(coord)] = height

# print(stack_ordered)
# exit()

def find_support(idx, above=False):
    # Given a brick, find all other bricks that are exactly one z above it,
    # and on the same x,y
    coords = [(x,y,z) for x,y,z,i in stack_ordered if i == idx]
    height = brick_heights[idx]
    zz = min([z for x,y,z,i in stack_ordered if i == idx])
    
    # and on the same x,y
    coords_around = [(x,y,z,i, "u" if z > zz else "d"
                      ) for x,y,z,i in stack_ordered if ((((x,y,z-brick_heights[i]) in coords) or ((x,y,z+height) in coords) and not above)) and i != idx]
    



    return coords_around
    # return [cords_up, cords_down]


# print(find_support(5))


# Part 1
if False:

    can_remove = 0

    for i in range(len(grid)):
        support = find_support(i)
        above = [x for x in support if x[4] == "u"]
        below = [x for x in support if x[4] == "d"]

        # if len(above) == 0:
        #     # print("Can Remove", i, grid[i])
        #     can_remove += 1
        #     pass
        # else:
        remove = True
        for x in above:
            s = find_support(x[3])
            below = [x for x in s if x[4] == "d" and x[3] != i]
            if len(below) == 0:
                # print("Can Remove", i, grid[i])
                remove = False
                break
        if remove:
            # print("Can Remove", i, grid[i])
            can_remove += 1


    print(can_remove)


## Part 2
    
cache = {}

def find_falling(idx, fallen):


    key = (idx, frozenset(fallen))
    if key in cache:
        return cache[key]

    fallen.add(idx)
    
    falling = set()
    supports = [x[3] for x in find_support(idx, above=True)]
    for s in supports:
        bricks_under_s = find_support(s)
        bricks_under_s = [x for x in bricks_under_s if x[4] == "d" and x[3] not in fallen]
        if len(bricks_under_s) == 0:
            falling.add(s)
        
            falling |= find_falling(s, fallen)

    cache[key] = falling | {idx}

    return falling

    

# Sort the bricks so the highest z is first
ns = [x[3] for x in sorted(stack_ordered, key=lambda x: x[2])]
# remove duplicates
ns = list(dict.fromkeys(ns))
print(ns)

total_fall = 0
for i, idx in enumerate(ns[:]):
    fallen = set()
    fall = find_falling(idx, fallen)
    total_fall += len(fall)
    print(i, idx, total_fall)

print(total_fall)







exit()

# exit()
good_idx = set()
for coord in grid:
    # For each x,y coordinate that it covers
    # Check if the height of the stack is the same as the miny + height
    # If it is, then it is the top of the stack
    idx = grid.index(coord)
    coords = [(x,y) for x,y,i ,h in stack_ordered if i == idx]
    print(coord, coords)

    all_coords = [x for x in stack_ordered if (x[0], x[1]) in coords]
    all_coords.sort(key=lambda x: -x[2])
    max_z = all_coords[0]
    
    # If idx is not same as the index of the coord
    # Then it is not the top of the stack

    if idx != max_z[3]:
        continue
    else:
        print("good", coord, max_z)


        
    # if all_good:
    #     good_idx.add(idx)
    #     print("good", coord)

# print(good_idx, grid)    
    # break
