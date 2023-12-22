lines = [[x for x in line.strip()] for line in open("16")]

# (x,y) coords, (y, x) velocity


def energize(beams):
    visited_tiles = set()
    beam_visited = (
        set()
    )  # Set of ((x,y), (x,y)) tuples, terminate when we hit a duplicate

    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            if beam in beam_visited:
                continue
            beam_visited.add(beam)
            # beam_visited.add(((beam[0][0], beam[0][1]), (-beam[1][0], -beam[1][1])))
            visited_tiles.add(beam[0])

            coords = beam[0]
            velocity = beam[1]

            s = lines[coords[1]][coords[0]]
            if s == "|":
                if velocity[0] != 0:
                    # Beams splits into two beams going to the side
                    # Check out of bounds
                    if coords[1] - 1 >= 0:
                        new_beams.append(((coords[0], coords[1] - 1), (0, -1)))

                    if coords[1] + 1 < len(lines):
                        new_beams.append(((coords[0], coords[1] + 1), (0, 1)))
                    continue
            if s == "-":
                if velocity[1] != 0:
                    # Beams splits into two beams going to the side
                    # Check out of bounds
                    if coords[0] - 1 >= 0:
                        new_beams.append(((coords[0] - 1, coords[1]), (-1, 0)))

                    if coords[0] + 1 < len(lines):
                        new_beams.append(((coords[0] + 1, coords[1]), (1, 0)))
                    continue
            if s == "/":
                if velocity[0] == 0:
                    if velocity[1] == 1:
                        velocity = (-1, 0)
                    else:
                        velocity = (1, 0)
                else:
                    if velocity[0] == 1:
                        velocity = (0, -1)
                    else:
                        velocity = (0, 1)

            if s == "\\":
                if velocity[0] == 0:
                    if velocity[1] == 1:
                        velocity = (1, 0)
                    else:
                        velocity = (-1, 0)
                else:
                    if velocity[0] == 1:
                        velocity = (0, 1)
                    else:
                        velocity = (0, -1)

            new_coords = (coords[0] + velocity[0], coords[1] + velocity[1])
            # If coords out of bounds, terminate
            if (
                new_coords[0] < 0
                or new_coords[0] >= len(lines)
                or new_coords[1] < 0
                or new_coords[1] >= len(lines[0])
            ):
                continue
            new_beams.append((new_coords, velocity))
        beams = new_beams
    return visited_tiles


# Print a grid the size of lines and mark the visited tiles
# for y in range(len(lines)):
#     for x in range(len(lines[0])):
#         if (x, y) in visited_tiles:
#             print("X", end="")
#         else:
#             print(" ", end="")
#     print()

beam_list = []

# Top down
beam_list.extend([((i, 0), (0, -1)) for i in range(len(lines[0]))])
# Bottom up
beam_list.extend([((i, len(lines) - 1), (0, 1)) for i in range(len(lines[0]))])
# Left to right
beam_list.extend([((0, i), (1, 0)) for i in range(len(lines))])
# Right to left
beam_list.extend([((len(lines[0]) - 1, i), (-1, 0)) for i in range(len(lines))])

max_visited = 0
for beam in beam_list:
    visited_tiles = energize([beam])
    if len(visited_tiles) > max_visited:
        max_visited = len(visited_tiles)
print(max_visited)
