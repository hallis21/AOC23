# Assuming the content from "./input.js" is now available as a string in `input_data`
input_data = open("4").read()

# Split the input data into sections
sections = input_data.split("\n\n")

# Extract seeds from the first section
seeds = [int(seed) for seed in sections[0].split(": ")[1].split()]

# Construct maps from the remaining sections
maps = []
for section in sections[1:]:
    map_ = []
    lines = section.strip().split(":\n")[1].strip().split("\n")
    for line in lines:
        map_.append([int(value) for value in line.split()])
    maps.append(map_)

# Initialize the lowest value to positive infinity
lowest_value = float('inf')

# Iterate over each map
for map_ in maps:
    # For each map, check the current values for a given seed index
    for seed_index in range(0, len(seeds), 2):
        # Initialize the ranges for the current seed index
        current_ranges = [[seeds[seed_index], seeds[seed_index] + seeds[seed_index + 1] - 1]]

        # Iterate over each mapping range in the current map
        for destination, source, map_range in map_:
            # Initialize a list to hold the new ranges after applying the current map
            new_ranges = []
            # Initialize a list to hold ranges that are left over after the map application
            left_over_ranges = []

            # Iterate over each current range
            for range_start, range_end in current_ranges:
                # Check if the current range overlaps with the source range of the map
                if range_start <= source + map_range - 1 and range_end >= source:
                    # Calculate the difference between destination and source
                    diff = destination - source
                    # Find the overlapping range
                    match_range_start = max(range_start, source)
                    match_range_end = min(range_end, source + map_range - 1)
                    # Add the transformed range to new_ranges
                    new_ranges.append([match_range_start + diff, match_range_end + diff])

                    # Add left-over ranges before and after the overlapping part
                    if range_start < source:
                        left_over_ranges.append([range_start, source - 1])
                    if range_end > source + map_range - 1:
                        left_over_ranges.append([source + map_range, range_end])
                else:
                    # If there's no overlap, add the current range to left_over_ranges
                    left_over_ranges.append([range_start, range_end])

            # Update current_ranges to left_over_ranges plus new_ranges for the next iteration
            current_ranges = left_over_ranges + new_ranges

        # Update the lowest value if a lower one is found
        for range_start, _ in current_ranges:
            if range_start < lowest_value:
                lowest_value = range_start

# Print the lowest value
print(lowest_value)
