from functools import reduce


lines = [
    [int(y.strip()) for y in x.split(":")[1].split()] for x in open("6").readlines()
]
races = list(zip(*lines))


ways = []
for race in races:
    t = race[0]
    min_dist = race[1]
    ds = []
    for x in range(0, t + 1):
        print("\r", x, "/", t, end="")
        dist = x * (t - x)
        if dist <= min_dist and len(ds) > 0:
            break
        if dist <= min_dist:
            continue
        ds.append(x * (t - x))
    ways.append(len(ds))


# multiply all ways
print(reduce(lambda x, y: x * y, ways))
