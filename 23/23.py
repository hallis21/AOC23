lines = [x.strip() for x in open("23")]


start = (1,0)

dirs = [(0,1, "v."), (1,0, ">."), (0,-1, "^."), (-1,0, "<.")]
# BFS
# (coord, visited)
queue = [(start, [])]

w,h = len(lines[0]), len(lines)
end = (w-2, h-1)

cache = {}
paths = []
while len(queue) > 0:
    if len(queue) % 1000 == 0:
        print(len(queue))
    next = queue.pop(0)
    cord = next[0]


    if cord == end:
        paths.append(next) 

    for dir in dirs:
        next_cord = (cord[0] + dir[0], cord[1] + dir[1])
        if next_cord in next[1]:
            continue
        if next_cord[0] < w and next_cord[0] >= 0 and next_cord[1] < h and next_cord[1] >= 0:
            if lines[next_cord[1]][next_cord[0]] != "#":
                visited = set(next[1]) | {cord}
                queue.append((next_cord, visited))


max_len = 0
for path in paths:
    if len(path[1]) > max_len:
        max_len = len(path[1])

print(max_len) 