lines = [line.strip() for line in open('11')]

# [print(l) for l in lines]
# Extend lines

extended_rows = []
extended_cols = []

# for i in range(2):
extended_rows = [i for i,l in enumerate(lines) if l.count(".") == len(l)]
lines = ["".join([l[i] for l in lines]) for i in range(len(lines[0]))]
    ## Rotate 90 degrees
extended_cols = [i for i,l in enumerate(lines) if l.count(".") == len(l)]
lines = ["".join([l[i] for l in lines]) for i in range(len(lines[0]))]

galaxies = []
total = len(lines)*len(lines[0])
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            galaxies.append((i,j))


# [print(l) for l in lines]
# print(galaxies)

# Make all unique pairs, order doesn't matter
pairs = [(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i+1, len(galaxies))]

# dist = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1])

def dist(a,b, extended_rows=extended_rows, extended_cols=extended_cols):
    l = abs(a[0]-b[0])+abs(a[1]-b[1])

    # If the index crosses over an extended row or col, add 1 million - 1

    for exr in extended_rows:
        if (a[0] < exr and b[0] > exr) or (a[0] > exr and b[0] < exr):
            l += 1000000-1

    for exc in extended_cols:
        if (a[1] < exc and b[1] > exc) or (a[1] > exc and b[1] < exc):
            l += 1000000-1
    return l


print(dist((0,0), (2,0), extended_rows=[1], extended_cols=[]))


print(sum(map(lambda x: dist(x[0], x[1]), pairs)))

# Find the length of the shortest path between all pairs