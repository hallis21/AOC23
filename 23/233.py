from collections import defaultdict
from matplotlib import pyplot as plt


lines = [x.strip() for x in open("23")]


# Find all intersections in the maze

start = (1,0)
w,h = len(lines[0]), len(lines)
end = (w-2, h-1)

intersections = [start, end]

for y in range(len(lines)):
    for x in range(len(lines[0])):
        # Replace ".>^v<" with "."
        if lines[y][x] in ".>^v<":
            lines[y] = lines[y][:x] + "." + lines[y][x+1:]


# an interseciton a point where a . is surrounded by more than 2 other .s
dirs = [(0,1, "v."), (1,0, ">."), (0,-1, "^."), (-1,0, "<.")]

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == ".":
            if x > 0 and x < len(lines[0]) - 1 and y > 0 and y < len(lines) - 1:
                count = 0
                for dir in dirs:
                    if lines[y + dir[0]][x + dir[1]] == ".":
                        count += 1
                if count > 2:
                    intersections.append((x,y))


# For each intersection, find all connected intersections and make a graph
# Since we are connectiong intersctions, there will be no cycles between them

# cord: {cord: dist}
network = dict()   
# print(intersections)
w,h = len(lines[0]), len(lines)



# print the grid, mark intersections as +



inter_paths = dict()
for intersection in intersections:
    inter_paths[intersection] = []
    network[intersection] = defaultdict(lambda: 0)
    # BFS
    # (coord, visited)

    queue = []
    # There should be atleast 2 paths from the intersection
    for dir in dirs:
        next_cord = (intersection[0] + dir[0], intersection[1] + dir[1])
        if next_cord[0] < w and next_cord[0] >= 0 and next_cord[1] < h and next_cord[1] >= 0:
            if lines[next_cord[1]][next_cord[0]] == ".":
                # queue.append((next_cord, [intersection]))
                inter_paths[intersection].append(next_cord)


# for intersection in intersections:
#     lines[intersection[1]] = lines[intersection[1]][:intersection[0]] + "+" + lines[intersection[1]][intersection[0]+1:]
#     for i,p in enumerate(inter_paths[intersection]):
#         lines[p[1]] = lines[p[1]][:p[0]] + str(i+1) + lines[p[1]][p[0]+1:]





# For each intersection, do DFS to find the path to the next inersection
# Can only move on "."s
# There should be no cycles so no point in using visited, only dont move back
    
for intersection in intersections:
    # DFS
    # (coord, visited, length)

    queue = []

    for initial in inter_paths[intersection]:
        # Check if the initial is an intersection, if it is, add 1 as the length
        if initial in intersections:
            network[intersection][initial] = 1
        else:
            queue.append((initial, intersection, 1))
        # There should only be one possible path from this since 
        # we use the inital which is offset to the first square of a direction


    while len(queue) > 0:
        cur_cord, prev_cord, length = queue.pop()

        for dir in dirs:
            next_cord = (cur_cord[0] + dir[0], cur_cord[1] + dir[1])
            if next_cord == prev_cord:
                continue
            # Ensure it is witihn bounds
            if next_cord[0] < w and next_cord[0] >= 0 and next_cord[1] < h and next_cord[1] >= 0:
                # If it is a ., add it to the queue
                if next_cord in intersections:
                    # Two paths can lead to the same intersection
                    # So do max of the two lengths
                    prev = network[intersection][next_cord]
                    network[intersection][next_cord] = max(prev, length+1)
                    network[next_cord][intersection] = max(prev, length+1)
                    # Remove the prev_cord from the inter_paths if it is there
                    # Since we have already found a path to it
                    if prev_cord in inter_paths[next_cord]:
                        inter_paths[next_cord].remove(prev_cord)
                    continue
                if lines[next_cord[1]][next_cord[0]] == ".":
                    queue.append((next_cord, cur_cord, length + 1))
                # If it is an intersection, add it to the network
    







# Using networkx draw the graph

import networkx as nx

G = nx.Graph()

for intersection in intersections:
    G.add_node(intersection, pos=intersection)

for intersection in intersections:
    for next in network[intersection]:
        G.add_edge(intersection, next, weight=network[intersection][next])


# All simple paths
paths = list(nx.all_simple_paths(G, start, end))

l = len(paths)
# Find the longest path by adding up the weights of the edges
max_path = 0
for i, path in enumerate(paths):

    if i % 1000 == 0:
        print(i, "/", l) 

    length = 0
    for i in range(len(path) - 1):
        length += network[path[i]][path[i+1]]
    max_path = max(max_path, length)

print(max_path)
exit()


pos=nx.get_node_attributes(G,'pos')
nx.draw(G, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.show()