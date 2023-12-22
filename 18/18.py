

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


