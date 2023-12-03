
print(sum([number for sublist in [[(lambda lst: [[(store.__setitem__("s", store["s"]*n), store["s"])[1] for n in lst[1:]] for store in [{"s":lst[0]}]][0][0])(l) for l in [[x[2] for x in set(l)]] if len(l) > 1] for sl in [n for n in [[list(map(lambda x: [(o[0], o[1][0][0], int("".join([*o[1:][0][0][1], *o[1:][0][1]]))) for o in [[(y[0], (lambda start, line: ([number for sublist in [[(start-len(x),x) for x in [(lambda line, start, width: list(reversed([n for n in [[[x, x.isdigit() or b.__setitem__("a", False)][0] for x in list(reversed(line))[width-start:] if b["a"]] for b in [{"a":True}]][0] if n.isdigit()])))(line, start, len(line))]], [(lambda line, start: [n for n in [[[x, x.isdigit() or b.__setitem__("a", False)][0] for x in line[start:] if b["a"]] for b in [{"a":True}]][0] if n.isdigit()])(line, start)]] for number in sublist]))(y[1], x[1][y[0]])) for y in z if type(y) == tuple] for z in x][0] if len(o) > 0], [(x,[l[1] for l in lines]) for x in map(lambda inp: [item for sublist in [coord for coord in [[(inp[0]+(-1+ii), inp[1]+(-1+i)) for i,y in enumerate(x) if y.isdigit()] for ii, x in enumerate([line[1][inp[1]-1: inp[1]+2] for line in inp[3]])] if len(coord) > 0] for item in sublist], [(y, x, s, lines[y-1:y+2]) for x, s in enumerate(line) if s != "." and not s.isdigit()])])) for y, line in lines] for lines in [[(i, x.strip()) for i,x in list(enumerate(open("3").readlines()))]]][0] if len(n) > 0] for l in sl]  for number in sublist]))

# result = [n[]]

# print(exec("return 1"))

exit()
symbols = []
gears = {}

for x in range(len(data)):
    for y in range(len(data[x])):
        if data[x][y] != "." and not data[x][y].isdigit():
            symbols.append((x, y, data[x][y]))
        


digits = set()

for symbol in symbols:
    x, y, s = symbol
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i >= 0 and x + i < len(data) and y + j >= 0 and y + j < len(data[x]):
                if data[x + i][y + j].isdigit():
                    digit = data[x + i][y + j]
                    l = 1
                    while y + j - l >= 0 and data[x + i][y + j - l].isdigit():
                        digit = data[x + i][y + j - l] + digit
                        l += 1
                    k = 1
                    while y + j + k < len(data[x]) and data[x + i][y + j + k].isdigit():
                        digit = digit + data[x + i][y + j + k]
                        k += 1

                    if s == "*" and (x + i, y + j - l + 1, digit) not in digits:
                        if str((x,y)) not in gears:
                            gears[str((x,y))] = []
                        gears[str((x,y))].append(digit)
                    
                    digits.add((x + i, y + j - l + 1, digit))


# List comprehension to multiply all numbers in a list without reduce


print(gears)
g_sum = 0
for g in gears:
    if len(gears[g]) >= 2:
        numbers = [int(x) for x in gears[g]]
        print(numbers)
        # Multiply all numbers together
        mult_sum = reduce(lambda x, y: x * y, numbers)
        g_sum += mult_sum

print(g_sum)
        
        



# Remove duplicate coordinates
digits = list(set(digits))

print(sum([int(x[2]) for x in digits]))

