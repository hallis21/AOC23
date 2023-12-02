# t1
print(sum([i + 1 for i, x in enumerate([(lambda x: not (x[0] > 12 or x[1] > 13 or x[2] > 14))((lambda x: tuple([max([y[i] for y in x]) for i in range(len(x[0]))]))((lambda yy: [tuple([max([y[i] for y in x]) for i in range(len(x[0]))]) for x in yy])([list(map((lambda x: (int(x[0]), 0, 0) if "red" in x else (0, int(x[0]), 0) if "green" in x else (0, 0, int(x[0]))),[t.split() for t in r.strip().split(",")],)) for r in g.split(";")]))) for g in [x.split(":")[1].strip() for x in open("2").readlines()]]) if x]))

# t2
print(sum([(lambda x: x[0] * x[1] * x[2])((lambda x: tuple([max([y[i] for y in x]) for i in range(len(x[0]))]))((lambda yy: [tuple([max([y[i] for y in x]) for i in range(len(x[0]))]) for x in yy])([list(map((lambda x: (int(x[0]), 0, 0) if "red" in x else (0, int(x[0]), 0) if "green" in x else (0, 0, int(x[0]))),[t.split() for t in r.strip().split(",")])) for r in g.split(";")]))) for g in [x.split(":")[1].strip() for x in open("2").readlines()]]))
