lines = [l.strip() for l in open("14").readlines()]




rocks = [0 for x in range(len(lines[0]))]
rocks_pos = []

rollers = []
roller_pos = []


# for ii,l in enumerate(lines):
#     for i in range(len(l)):
#         if l[i] == "O":
#             roller_pos.append((i, ii))

# print(roller_pos)


# Part 1
# for ii,l in enumerate(lines):
#     for i in range(len(l)):
#         if l[i] == "O":
#             roller_pos.append((i, rocks[i]))
#             rollers.append(rocks[i])
#             rocks[i] += 1
#         elif l[i] == "#":
#             rocks[i] = (ii+1)
#             rocks_pos += [(i, ii)]


for ii,l in enumerate(lines):
    for i in range(len(l)):
        if l[i] == "O":
            roller_pos.append((i, ii))
        elif l[i] == "#":
            rocks_pos += [(i, ii)]



def roll_north(rocks, rollers):
    # since roll north, sort rollers by y
    rollers.sort(key=lambda x: x[1])

    current_max = [[] for x in range(len(lines[0]))]

    for rock in rocks:
        current_max[rock[0]].append(rock[1])

    print(current_max)
    for i, roller in enumerate(rollers):
        row_max = current_max[roller[0]]

        locs = [x for x in row_max if x < roller[1]]
        new_loc = 0 if len(locs) == 0 else max(locs)+1

        rollers[i] = (roller[0], new_loc)
        current_max[roller[0]].append(new_loc)

        print(roller, row_max, locs, new_loc)



def roll_south(rocks, rollers):
    # since roll south, sort rollers by y reversed
    current_max = [0 for x in range(len(lines[0]))]
    rollers.sort(key=lambda x: x[1], reverse=True)
    



roll_north(rocks_pos, roller_pos)
# print(rocks_pos)
print(roller_pos)
# print(sum([len(lines)-x for x in rollers]))