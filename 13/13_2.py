

patterns = [x for x in open("13").read().split('\n\n') if x]
all_overlaps_horizontal = []
all_overlaps_vertical = []

prev_horizontal = []
prev_vertical = []



for i, pattern in enumerate(patterns):
    lines = [x.strip() for x in pattern.split('\n') if x != '']

    transposed_lines = ["".join(x) for x in list(zip(*lines))]

    overlaps_horizontal = []
    overlaps_vertical = []
    

    # Check overlap vertical line
    l = len(lines[0])
    for i in range(l)[1:]:
        overlap = True
        for line in lines:

            # Left side should be equal length to right side
            len_right = l - i
            len_left = i
            left_start_i = max(len_left - len_right, 0)
            if not (list(line[left_start_i:i]) == list(reversed(line[i:i+i]))):
                overlap = False
                break
        if overlap:
            overlaps_vertical.append(i)


    l = len(lines)
    for i in range(l)[1:]:
        overlap = True
        for line in transposed_lines:

            # Left side should be equal length to right side
            len_right = l - i
            len_left = i
            left_start_i = max(len_left - len_right, 0)
            print(line[left_start_i:i], line[i:i+i])

            if not (list(line[left_start_i:i]) == list(reversed(line[i:i+i]))):
                overlap = False
                break
        if overlap:
            overlaps_horizontal.append(i)
    prev_horizontal.append(overlaps_horizontal)
    prev_vertical.append(overlaps_vertical)


for ip, pattern in enumerate(patterns):
    for ii in range(len(pattern)):
        overlaps_horizontal = []
        overlaps_vertical = []
        
    
        new_pattern = list(pattern)
        if new_pattern[ii] not in '.#':
            continue
        if new_pattern[ii] == '#':
            new_pattern[ii] = '.'
        elif new_pattern[ii] == '.':
            new_pattern[ii] = '#'

        new_pattern = "".join(new_pattern)

        lines = [x.strip() for x in new_pattern.split('\n') if x != '']

        [print(x) for x in lines]

        transposed_lines = ["".join(x) for x in list(zip(*lines))]


    
        # Check overlap vertical line
        l = len(lines[0])
        for i in range(l)[1:]:
            overlap = True
            for line in lines:

                # Left side should be equal length to right side
                len_right = l - i
                len_left = i
                left_start_i = max(len_left - len_right, 0)
                if not (list(line[left_start_i:i]) == list(reversed(line[i:i+i]))):
                    overlap = False
                    break
            if overlap:
                if i in prev_vertical[ip]:
                    continue
                overlaps_vertical.append(i)


        l = len(lines)
        for i in range(l)[1:]:
            overlap = True
            for line in transposed_lines:

                # Left side should be equal length to right side
                len_right = l - i
                len_left = i
                left_start_i = max(len_left - len_right, 0)

                if not (list(line[left_start_i:i]) == list(reversed(line[i:i+i]))):
                    overlap = False
                    break
            if overlap:
                if i in prev_horizontal[ip]:
                    continue
                overlaps_horizontal.append(i)
        if len(overlaps_horizontal) > 0 or len(overlaps_vertical) > 0:
            all_overlaps_horizontal.extend(overlaps_horizontal)
            all_overlaps_vertical.extend(overlaps_vertical)
            print(overlaps_horizontal, overlaps_vertical, ii)
            break
            
print(all_overlaps_vertical)
print(all_overlaps_horizontal)

print(sum(all_overlaps_vertical) + sum(all_overlaps_horizontal)*100)