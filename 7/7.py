from functools import reduce


lines = [x.strip() for x in open("7").readlines() if x != "\n"]
instructions = [x for x in lines[0]]

nodes = [[(y[0], y[2][1:-1], y[3][:-1]) for y in [x.split(" ")]] for x in lines[1:]]

nodes = [item for sublist in nodes for item in sublist]

m = {}

for x in nodes:
    m[x[0]] = (x[1], x[2])

# A list of all nodes that end in A
cur_pos = [x for x in m if x[-1] == "A"]
print(len(cur_pos), len(instructions))




# loop over instructions indefinitely until we reach ZZZ
i = 0
steps = 0
rounds = 0

rs = [0 for x in cur_pos]

while True:
    # if we reach XXZ, we're done
    zs = [x for x in cur_pos if x[-1] == "Z"]
    if len(cur_pos) == len(zs):
        break
    
    if i >= len(instructions):
        i = 0

        rounds += 1
        # Mark rs with rounds for the positions that end in Z
        for x in cur_pos:
            if x[-1] == "Z":
                rs[cur_pos.index(x)] = rounds
        if all([x != 0 for x in rs]):
            r =[x for x in rs]
            # Print the product of the rounds
            print(reduce(lambda x, y: x * y, r)*len(instructions))
            break
            
    
    instruction = instructions[i]

    if instruction == "L":
        cur_pos = [m[x][0] for x in cur_pos]
    else :
        cur_pos = [m[x][1] for x in cur_pos]
    i += 1
    steps += 1
    if (steps % 1000000 == 0):
        print(steps)

print(steps)

