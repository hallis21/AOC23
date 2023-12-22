lines = [line.strip().split() for line in open('12')]


cache = {}

def recurse_dumb(hots, nums):
    if len(hots) == 1:
        if hots[0] == '?':
            return ["#", "."] 
        else:
            return [hots[0]]



    if hots[0] == '?':
        # For each string in recurse(hots[1:]) create a new string where hots[0] is replaced with "#" or "."
        return [y+x  for x in recurse(hots[1:], nums) for y in ["#", "."]]
    else:
        return [hots[0] + x for x in recurse(hots[1:], nums)]


def recurse(hots, nums):
    if hots == "":
        # Is match if nums is empty also
        return 1 if len(nums) == 0 else 0

    if len(nums) == 0:
        # If there are still broken hotsprings, it's not a match
        return 1 if "#" not in hots else 0

    total = 0


    
    key = (hots, nums)

    if key in cache:
        return cache[key]

    # two scenarios, remove num or not



    # if it is . then we do not remove num
    if hots[0] == '.':
        total += recurse(hots[1:], nums)
    # if it is # then we remove num if the next num is possible
    if hots[0] == '#':
        # Check if the whole 'num' of # can fit at the current position

        if nums[0] <= len(hots) and "." not in hots[:nums[0]] and (nums[0] == len(hots) or hots[nums[0]] != "#"):
            total += recurse(hots[nums[0] + 1:], nums[1:])
    
    if hots[0] == '?':
        # Pretend is .
        total += recurse(hots[1:], nums)
        # Pretend is #
        if nums[0] <= len(hots) and "." not in hots[:nums[0]] and (nums[0] == len(hots) or hots[nums[0]] != "#"):
            total += recurse(hots[nums[0] + 1:], nums[1:])

    cache[key] = total
    return total


    
    
all_matches = 0
for i, line in enumerate(lines):
    hots = line[0]
    nums = [int(x) for x in line[1].split(',')]

    new_hots = []
    combos = recurse(((hots+"?")*5)[:-1], tuple(nums*5))
    # print(len(combos))

    # matches = 0

    # for combo in combos:
    #     brokes = [len(x) for x in combo.split('.') if x != ""]
    #     if brokes == nums:
    #         matches += 1
    
    all_matches += combos
    print(i, combos)
    # break
print("****REDACTED****")


