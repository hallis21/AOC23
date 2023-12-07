lines = [x.strip() for x in open('4').readlines() if x.strip() != '']

seeds = [int(x) for x in lines[0].split(':')[1].strip().split(" ")]
seeds = [(x,(y+x)-1) for x,y in zip(seeds[::2], seeds[1::2])]

maps = []
for l in lines[1:]:
    if l[0].isdigit():
        maps[-1].append([int(x) for x in l.split(" ")])
    else:
        maps.append([])
# Translate maps to change
new_maps = [[((y[1], y[1]+y[2]), y[1]-y[0] ) for y in x] for x in maps]



ranges_to_check = seeds

for m in new_maps:
    ranges_for_next = []
    for r in ranges_to_check:
        mapped = False
        new_ranges = []
        left_over_ranges = []
        for sub_map in m:
            r_start, r_end = r
            map_start, map_end = sub_map[0]
            map_diff = sub_map[1]

            # Check if there is an overlap with the sub_map range
            if r_start <= map_end and r_end >= map_start:
                mapped = True
                # Calculate new overlapping range
                new_start = max(r_start, map_start) + map_diff
                new_end = min(r_end, map_end) + map_diff
                new_ranges.append((new_start, new_end))

                # Find leftover range before the sub_map range
                if r_start < map_start:
                    ranges_for_next.append((r_start, map_start - 1))

                # Find leftover range after the sub_map range
                if r_end > map_end:
                    ranges_for_next.append((map_end + 1, r_end))
        if not mapped:
            left_over_ranges.append(r)

        # Set ranges_to_check to new_ranges for the next sub_map iteration
        ranges_to_check = new_ranges
        ranges_to_check.extend(left_over_ranges)

    # Combine leftover ranges with new ranges for next map iteration
    ranges_for_next.extend(ranges_to_check)
        
                

print(ranges_for_next)
print(min([x[0] for x in ranges_for_next]))
    

                
            