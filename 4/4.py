# numbers = [[set([l for l in y.strip().split(" ") if l != ""]) for y in x.split(":")[1].split("|")] for x in open("4").readlines()]

make_score = lambda x: (1 if x == 1 else ((2 if x > 0 else 0)**(x-1 if x > 1 else 1)))

score = [(len(x[0])+len(x[1]))-len(x[0].union(x[1])) for x in [[set([l for l in y.strip().split(" ") if l != ""]) for y in x.split(":")[1].split("|")] for x in open("4").readlines()]]

# 1
print(sum([(lambda x: (1 if x == 1 else ((2 if x > 0 else 0)**(x-1 if x > 1 else 1))))(x) for x in [(len(x[0])+len(x[1]))-len(x[0].union(x[1])) for x in [[set([l for l in y.strip().split(" ") if l != ""]) for y in x.split(":")[1].split("|")] for x in open("4").readlines()]]]))

# 2
flatten = lambda *n: (e for a in n
    for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
calc = lambda i, scores: 1 if scores[i] == 0 else [calc(ii+i, scores) if ii != 0 else 1 for ii,x in enumerate(scores[i:i+score[i]+1])]
s = [calc(i, score) for i in range(len(score))]


print(sum(list(flatten(s))))