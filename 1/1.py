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



# findNumber = lambda s: [n for n in [tans[s[x:]] if s[x:] in tans.keys() else False for x in range(len(s))] if n != False]


# n1s = [[l[0] if type(l) == list else l for l in [number for number in [int(line[i]) if line[i].isnumeric() else (lambda s: [n for n in [{ "one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,}[s[x:]] if s[x:] in [ "one",  "two",  "three", "four", "five", "six", "seven", "eight", "nine"] else False for x in range(len(s))] if n != False])(line[:i+1]) for line in [l] for i in [n for n in range(len(l))]] if number != []]][0] for l in lines]
# n2s = [[l[0] if type(l) == list else l for l in [number for number in [int(line[i]) if line[i].isnumeric() else (lambda s: [n for n in [{"one": 1,"two": 2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,}[s[x:]] if s[x:] in [ "one",  "two",  "three", "four", "five", "six", "seven", "eight", "nine"] else False for x in range(len(s))] if n != False])(line[:i+1]) for line in [l] for i in [n for n in range(len(l))]] if number != []]][-1] for l in lines]

print(sum([int(str(x[0])+str(x[1])) for x in zip([[l[0] if type(l) == list else l for l in [number for number in [int(line[i]) if line[i].isnumeric() else (lambda s: [n for n in [{ "one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,}[s[x:]] if s[x:] in [ "one",  "two",  "three", "four", "five", "six", "seven", "eight", "nine"] else False for x in range(len(s))] if n != False])(line[:i+1]) for line in [l] for i in [n for n in range(len(l))]] if number != []]][0] for l in lines], [[l[0] if type(l) == list else l for l in [number for number in [int(line[i]) if line[i].isnumeric() else (lambda s: [n for n in [{"one": 1,"two": 2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,}[s[x:]] if s[x:] in [ "one",  "two",  "three", "four", "five", "six", "seven", "eight", "nine"] else False for x in range(len(s))] if n != False])(line[:i+1]) for line in [l] for i in [n for n in range(len(l))]] if number != []]][-1] for l in lines])]))



# print([x for x in open("i.txt").readlines()])