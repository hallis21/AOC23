s = open('15').read()




n = [x for x in  s.split(',')]
n = [x for x in n]

nums = []

for p in n:
    s = 0
    # if len(p) == 2:
    #     s = int(p[1]) 
    # else:
    #     p[0] = p[0][:-1]
    for letter in p:
        # ASCII value of letter
        val = ord(letter)
        s += val
        s *= 17
        s %= 256
    nums.append(s)

print(sum(nums))