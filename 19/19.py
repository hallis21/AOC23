inp = open("19").read().split("\n\n")


buckets = {
    "A": [],
    "R": [],
}

rules = {}
for line in inp[0].split("\n"):
    parts = line.split("{")
    p = [x.split(":") if ":" in x else x for x in parts[1][:-1].split(",")]
    
    for i, pp in enumerate(p):
        if type(pp) == list:
            p[i] = ((pp[0][0], pp[0][1], int(pp[0][2:])), pp[1])
    rules[parts[0]] = p
    buckets[parts[0]] = []
    
parts = []

for line in inp[1].split("\n"):
    # {x=1,y=2}
    parts.append({x.split("=")[0]:int(x.split("=")[1]) for x in line[1:-1].split(",")})

buckets["in"].extend(parts)


while len(buckets["A"]) + len(buckets["R"]) < len(parts):
    # Go through the buckets and run the rules
    pass

    for bucket in buckets:
        if bucket == "A" or bucket == "R":
            continue
        bparts = buckets[bucket]
        brules = rules[bucket]
        for parti in range(len(bparts)):
            part = bparts.pop(0)
            for rule in brules:
                if type(rule) == str:
                    # Place the part in the bucket
                    buckets[rule].append(part)
                    continue
                if rule[0][0] in part:
                    sign = rule[0][1]
                    n = rule[0][2]
                    to_eval = f"{part[rule[0][0]]} {sign} {n}"
                    r = eval(to_eval)
                    if r:
                        buckets[rule[1]].append(part)
                        break

ps = [sum([y[1] for y in x.items()]) for x in buckets["A"]]
print(ps)
print(sum(ps))


# 398693