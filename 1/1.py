lines = open("i.txt").readlines()

values = []

tans = {
    "one": 1,
    "two": 2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

for l in lines:
    first =''
    last = ''
    l1 = ''
    l2 = ''

    for leter in l:
        try:
            first = int(leter)
            break
        except:
            l1 += leter
            for t in tans:
                if t in l1:
                    first = tans[t]
                    break
            if first != '': break
    print(first)
  
    rl = "".join([x for x in reversed(l)])
    for i, leter in enumerate(reversed(l)):
        try:
            last = int(leter)
            
            break
        except:
            l2 = "".join([x for x in reversed(rl[:i+1].strip())])
            print(l2, rl[i])
            for t in tans:
                if t in l2:

                    last = tans[t]
                    break
            if last != '': break
    print(last)


    values.append(int(str(first)+str(last)))
print(sum(values))

