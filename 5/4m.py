lines = [x.strip() for x in open('4').readlines() if x.strip() != '']

seeds = [int(x) for x in lines[0].split(':')[1].strip().split(" ")]

maps = []
for l in lines[1:]:
    if l[0].isdigit():
        maps[-1].append([int(x) for x in l.split(" ")])
    else:
        maps.append([])

new_maps = [[(y[1]-y[0], (y[1], y[1]+y[2])) for y in x] for x in maps]



# from asyncio import sleep
from threading import Thread, Lock
from math import inf
from time import sleep
progress = [0] * (len(seeds) // 2)

def check_seed_range(new_maps, seed_start, seed_length, min_num, lock, i):
    # Local print function to avoid mixing output from different threads
     

    for ii, x in enumerate(range(seed_start, seed_start + seed_length)):
        progress[i] = (ii*1000) // seed_length
        stack = [(x, 0)]
        while stack:
            n, m_i = stack.pop()
            if m_i == len(new_maps):
                with lock:
                    min_num[0] = min(min_num[0], n)
                continue

            m = new_maps[m_i]
            checked = False

            for row in m:
                if n >= row[1][0] and n < row[1][1]:
                    checked = True
                    stack.append((n - row[0], m_i + 1))

            if not checked:
                stack.append((n, m_i + 1))

def check_iterative_multithreaded(new_maps, seeds):
    threads = []
    min_num = [inf]  # Use list to hold the minimum number so it can be updated by threads
    lock = Lock()  # Lock to control access to shared resources

    pairs = [x for x in zip(seeds[::2], seeds[1::2])]
    new_pairs = []
    for start, length in pairs:
        for i in range(0, length, 50000000):
            new_pairs.append((start+i, min(50000000, length-i)))
    global progress
    progress = [0] * (len(new_pairs))
    

    for i, (seed_start, seed_length) in enumerate(new_pairs):

        
        print(f"Starting thread {i} {(len(new_pairs))}")
        


        thread = Thread(target=check_seed_range, args=(new_maps, seed_start, seed_length, min_num, lock, i))
        threads.append(thread)
        thread.start()

    while any([thread.is_alive() for thread in threads]):
        # Print the progress of each thread
        print(f"\rProgress: {str(progress)}", end='')
        # Wait for 0.1 seconds
        sleep(0.1)

    for thread in threads:
        thread.join()

    return min_num[0]


result = check_iterative_multithreaded(new_maps, seeds)
print("Minimum number found:", result)
