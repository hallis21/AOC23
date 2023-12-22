

patterns = [x for x in open("13").read().split('\n\n') if x]
overlaps_horizontal = []
overlaps_vertical = []

for pattern in patterns:
    lines = [x.strip() for x in pattern.split('\n') if x != '']

    transposed_lines = ["".join(x) for x in list(zip(*lines))]


    
    print(lines)

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
            
print(overlaps_vertical)
print(overlaps_horizontal)

print(sum(overlaps_vertical) + sum(overlaps_horizontal)*100)