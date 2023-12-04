
# 1
print(sum([(lambda x: (1 if x == 1 else ((2 if x > 0 else 0)**(x-1 if x > 1 else 1))))(x) for x in [(len(x[0])+len(x[1]))-len(x[0].union(x[1])) for x in [[set([l for l in y.strip().split(" ") if l != ""]) for y in x.split(":")[1].split("|")] for x in open("4").readlines()]]]))

# # # 2

print([len([list(funcs["a"]["flat"]([funcs["a"]["calc"](i, score) for i in range(len(score))])) for funcs in [[[xx["a"].__setitem__("flat", lambda *n: (e for a in n
    for e in ((xx["a"]["flat"])(*a) if isinstance(a, (tuple, list)) else (a,)))), xx["a"].__setitem__("calc", lambda i, scores: 1 if scores[i] == 0 else [(xx["a"]["calc"])(ii+i, scores) if ii != 0 else 1 for ii,x in enumerate(scores[i:i+score[i]+1])])
      ,xx ][2] for xx in [{"a":{}}]][0]]][0]) for score in [[(len(x[0])+len(x[1]))-len(x[0].union(x[1])) for x in [[set([l for l in y.strip().split(" ") if l != ""]) for y in x.split(":")[1].split("|")] for x in open("4").readlines()]]]][0])

