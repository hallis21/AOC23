input_data = open("4").read()

sections = input_data.split("\n\n")


lines = [x.strip() for x in open('4').readlines() if x.strip() != '']

seeds = [int(x) for x in lines[0].split(':')[1].strip().split(" ")]


maps = []
for l in lines[1:]:
    if l[0].isdigit():
        maps[-1].append([int(x) for x in l.split(" ")])
    else:
        maps.append([])


low = float('inf')

for i in range(0, len(seeds), 2):
    check_next_map = [[seeds[i], seeds[i] + seeds[i + 1] - 1]]

    for m in maps:
        for_next_map = []
        for dest, source, map_range in m:
            overflow = []
            for range_start, range_end in check_next_map:
                if range_start < source + map_range and range_end >= source:
                    diff = dest - source
                    start = max(range_start, source)
                    end = min(range_end, source + map_range - 1)
                    for_next_map.append([start + diff, end + diff])

                    if range_start < source:
                        overflow.append([range_start, source - 1])

                    if range_end >= source + map_range:
                        overflow.append([source + map_range, range_end])
                else:
                    overflow.append([range_start, range_end])
            check_next_map = overflow

        check_next_map.extend(for_next_map)
    lowest = min([x[0] for x in check_next_map])
    low = lowest if lowest < low else low


print(low)