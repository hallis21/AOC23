neigboors = {
    "|": lambda x, y: [
        ((x, y - 1), ("|", "F", "7")),
        ((x, y + 1), ("|", "L", "J")),
    ],
    "-": lambda x, y: [
        (
            (x + 1, y),
            (
                "-",
                "J",
                "7",
            ),
        ),
        ((x - 1, y), ("-", "F", "L")),
    ],
    "L": lambda x, y: [
        ((x + 1, y), ("-", "J", "7")),
        ((x, y - 1), ("|", "F", "7")),
    ],
    "J": lambda x, y: [
        ((x - 1, y), ("-", "F", "L")),
        ((x, y - 1), ("|", "7", "F")),
    ],
    "F": lambda x, y: [
        ((x + 1, y), ("-", "J", "7")),
        ((x, y + 1), ("|", "L", "J")),
    ],
    "7": lambda x, y: [
        ((x - 1, y), ("-", "F", "L")),
        ((x, y + 1), ("|", "L", "J")),
    ],
}


lines = [
    [(x, y, s) for x, s in enumerate(line.strip())]
    for y, line in enumerate(open("10").readlines())
]

dist = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

start = (1, 1)
# Find "S"
for y, line in enumerate(lines):
    for x, s in enumerate(line):
        if s[2] == "S":
            start = (x, y)
            break

# Find out what pipe start is
start_ns = [
    ("1", start[0] + 1, start[1], ("J", "-", "7")),
    ("2", start[0] - 1, start[1], ("-", "F", "L")),
    ("3", start[0], start[1] + 1, ("|", "F", "7")),
    ("4", start[0], start[1] - 1, ("|", "7", "F")),
]

dist[start[1]][start[0]] = 1

ns = [(lines[y][x], 1) for _, x, y, s in start_ns if lines[y][x][2] in s]

while len(ns) > 0:
    n, d = ns.pop(0)
    d += 1
    dist[n[1]][n[0]] = d

    nn = neigboors[n[2]](n[0], n[1])
    # lines

    ns += [
        (x, d)
        for x, s in [(lines[cord[1]][cord[0]], s) for cord, s in nn]
        if x[2] in s and dist[x[1]][x[0]] == 0
    ]

## Print dist with same width for all numbers
# for line in dist:
#    print(" ".join([str(x).rjust(3) for x in line]))

# print(max([max(x) for x in dist])-1)

# Set . for all pipes which are 0 in dist
new_lines = []
for y, line in enumerate(lines):
    new_lines.append([])
    for x, s in enumerate(line):
        if dist[y][x] == 0:
            new_lines[-1].append(".")
        else:
            new_lines[-1].append(s[2])

m = [[y for y in x] for x in new_lines]


new_m = []
# Extend M with new lines and columns every other line
# new_m.append([" " for _ in range(len(m[0]) * 2)] + [" "])
for i, line in enumerate(m):
    n_m = [" "]
    for j, s in enumerate(line):
        n_m.append(s)
        n_m.append(" ")
    new_m.append(n_m)

    new_m.append([" " for _ in range(len(line) * 2)] + [" "])


new_m_copy = [[y for y in x] for x in new_m]
for i, line in enumerate(new_m_copy):
    for j, s in enumerate(line):
        if s == "|":
            new_m[i - 1][j] = "|"
            new_m[i + 1][j] = "|"
        if s == "-":
            new_m[i][j - 1] = "-"
            new_m[i][j + 1] = "-"
        if s == "L":
            new_m[i][j + 1] = "-"
            new_m[i - 1][j] = "|"
        if s == "J":
            new_m[i][j - 1] = "-"
            new_m[i - 1][j] = "|"
        if s == "F":
            new_m[i][j + 1] = "-"
            new_m[i + 1][j] = "|"
        if s == "7":
            new_m[i][j - 1] = "-"
            new_m[i + 1][j] = "|"

        if s == ".":
            new_m[i][j] = "X"


# [print(x) for x in new_m]


# Start in (0,0) and do bfs, set all visited to O
# Do not cross pipes

start = (0, 0)


<<<<<<< HEAD
def check_coord(x, y, i):

    # If we are out of bounds
    if x < 0 or y < 0 or y >= len(new_m) or x >= len(new_m[y]):
        return False
    # If one of the pipes return
    if new_m[y][x] in ["|", "-", "L", "J", "F", "7", "S"]:
        return
    # Set to 0
    new_m[y][x] = "0"

    neigboorss = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
    for n in neigboorss:
        # Check if we are out of bounds
        if n[0] < 0 or n[1] < 0 or n[1] >= len(new_m) or n[0] >= len(new_m[n[1]]):
            continue
        if new_m[n[1]][n[0]] == "0":
            continue

        check_coord(n[0], n[1],i + 1)


import sys

sys.setrecursionlimit(1500000)
# print(sys.getrecursionlimit())

check_coord(0, 0, 0)


# from collections import deque

# checked = [[False for _ in range(len(new_m[0]))] for _ in range(len(new_m))]
# def check_coord(x, y):
#     queue = deque([(x, y)])

#     i = 0
#     while queue:
#         i += 1
        
#         x, y = queue.popleft()

#         # If we are out of bounds
#         if x < 0 or y < 0 or y >= len(new_m) or x >= len(new_m[y]):
#             continue
#         # If one of the pipes return
#         if new_m[y][x] in ["|", "-", "L", "J", "F", "7", "S"]:
#             continue


#         if checked[y][x]:
#             continue
#         checked[y][x] = True
#         # Set to 0
#         new_m[y][x] = "0"

#         neigboorss = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
#         for n in neigboorss:
#             # Check if we are out of bounds
#             if n[0] < 0 or n[1] < 0 or n[1] >= len(new_m) or n[0] >= len(new_m[n[1]]):
#                 continue
#             if new_m[n[1]][n[0]] == "0":
#                 continue

#             queue.append(n)


# check_coord(0, 0)
=======
# def check_coord(x, y, i):
#     if i > 100:
#         return
#     # If we are out of bounds
#     if x < 0 or y < 0 or y >= len(new_m) or x >= len(new_m[y]):
#         return False
#     # If one of the pipes return
#     if new_m[y][x] in ["|", "-", "L", "J", "F", "7"]:
#         return
#     # Set to 0
#     new_m[y][x] = "0"

#     neigboorss = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
#     for n in neigboorss:
#         # Check if we are out of bounds
#         if n[0] < 0 or n[1] < 0 or n[1] >= len(new_m) or n[0] >= len(new_m[n[1]]):
#             continue
#         if new_m[n[1]][n[0]] == "0":
#             continue

#         check_coord(n[0], n[1],i + 1)


# import sys

# sys.setrecursionlimit(1500000)
# # print(sys.getrecursionlimit())

# check_coord(0, 0, 0)


from collections import deque

checked = [[False for _ in range(len(new_m[0]))] for _ in range(len(new_m))]
def check_coord(x, y):
    queue = deque([(x, y)])

    i = 0
    while queue:
        i += 1
        
        x, y = queue.popleft()

        # If we are out of bounds
        if x < 0 or y < 0 or y >= len(new_m) or x >= len(new_m[y]):
            continue
        # If one of the pipes return
        if new_m[y][x] in ["|", "-", "L", "J", "F", "7", "S"]:
            continue


        if checked[y][x]:
            continue
        checked[y][x] = True
        # Set to 0
        new_m[y][x] = "0"

        neigboorss = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
        for n in neigboorss:
            # Check if we are out of bounds
            if n[0] < 0 or n[1] < 0 or n[1] >= len(new_m) or n[0] >= len(new_m[n[1]]):
                continue
            if new_m[n[1]][n[0]] == "0":
                continue

            queue.append(n)


check_coord(0, 0)
>>>>>>> c7596288908ff78de9995320364bf9a536290157


# [print(x) for x in new_m]
with open("10_out", "w") as f:
    for line in new_m:
        f.write("".join(line) + "\n")

# Count all X in new_m
print(sum([x.count("X") for x in new_m]))
