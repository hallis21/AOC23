lines = [[int(x) for x in x.split()] for x in open("9").readlines()]


# find diffrences between each item, so x[i] - x[i-1] ...
find_diffrences = lambda x: [x[i] - x[i - 1] for i in range(1, len(x))]


def fill_inn(y, x):
    y.append(x[-1] + y[-1])


def fill_inn2(y, x):
    # print(y, x)
    y.insert(0,  y[0]-x[0] )


s = []
ss = []

for line in lines:
    cur_lines = [line]
    while [x for x in cur_lines[-1] if x != 0]:
        cur_lines.append(find_diffrences(cur_lines[-1]))

    cur_lines = cur_lines[::-1]
    ## Add 0 to the last line
    for i, line in enumerate(cur_lines):
        if i == 0:
            cur_lines[i].insert(0, 0)
            cur_lines[i].append(0)
        else:
            fill_inn(line, cur_lines[i - 1])
            fill_inn2(line, cur_lines[i - 1])

    s.append(cur_lines[-1][-1])
    ss.append(cur_lines[-1][0])

print(sum(ss), sum(s))
