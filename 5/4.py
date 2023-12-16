lines = [x.strip() for x in open('4').readlines() if x.strip() != '']

seeds = [int(x) for x in lines[0].split(':')[1].strip().split(" ")]


maps = []
for l in lines[1:]:
    if l[0].isdigit():
        maps[-1].append([int(x) for x in l.split(" ")])
    else:
        maps.append([])
# Translate maps to change

new_maps = [[(y[1]-y[0], (y[1], y[1]+y[2])) for y in x] for x in maps]

max_minus_per_level = [min([y[0] for y in x]) for x in new_maps]
max_minus = [sum(max_minus_per_level[:i+1]) for i in range(len(max_minus_per_level))][::-1]





inf = float('inf')
l = len(new_maps)
def check_iterative(new_maps, seeds):
    # Initialize the minimum number to a very large value
    min_num = inf
    # Print the range index
    for seed_start, seed_length, i in zip(seeds[::2], seeds[1::2], range(len(seeds[::2]))):
        print(i)
        for ii, x in enumerate(range(seed_start, seed_start + seed_length)):
            # Print \r to overwrite the previous line
            print("\r", ii, "/", seed_length, ii/seed_length, end="")


            # Stack to keep track of the state; each state is a tuple (n, m_i)
            stack = [(x, 0)]
            
            while stack:
                n, m_i = stack.pop()
                
                if m_i == len(new_maps):
                    # If we reach the end of new_maps, update min_num if necessary
                    min_num = min(min_num, n)
                    continue
                
                m = new_maps[m_i]
                checked = False
                
                for row in m:
                    if n >= row[1][0] and n < row[1][1]:
                        checked = True
                        # Push the next state onto the stack instead of calling recursively
                        stack.append((n - row[0], m_i + 1))
                
                if not checked:
                    # If no row was checked, push the next map onto the stack
                    stack.append((n, m_i + 1))
    
    return min_num

# Assuming new_maps and seeds are defined elsewhere in your code
result = check_iterative(new_maps, seeds)
print(result)