def is_valid_sequence(sequence, nums):
    counts = [len(block) for block in sequence.split('.') if block]
    return counts == nums

def recurse(hots, nums, index=0, current_sequence=None):
    if current_sequence is None:
        current_sequence = []

    # Base case: if the current index is equal to the length of hots,
    # check if the current sequence is valid.
    if index == len(hots):
        if is_valid_sequence(''.join(current_sequence), nums):
            return 1
        return 0

    # If the current character is not a wildcard, just continue to the next character.
    if hots[index] != '?':
        current_sequence.append(hots[index])
        count = recurse(hots, nums, index + 1, current_sequence)
        current_sequence.pop()  # Backtrack
        return count

    # Try with a '#' and then with a '.' for the current wildcard character.
    count = 0
    for char in ['#', '.']:
        current_sequence.append(char)
        count += recurse(hots, nums, index + 1, current_sequence)
        current_sequence.pop()  # Backtrack
    return count

def calculate_matches(lines):
    all_matches = 0
    for i, line in enumerate(lines):
        hots, num_str = line
        nums = list(map(int, num_str.split(',')))

        # Call the optimized recursive function.
        matches = recurse(((hots))[:-1], nums)
        all_matches += matches
        print(i, matches)
    return all_matches

# Example usage:
lines = [line.strip().split() for line in open('12')]
print(calculate_matches(lines))