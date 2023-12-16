from functools import reduce


data = [
    line.strip() for line in open("3").readlines()
]



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

