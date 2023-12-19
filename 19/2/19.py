inp = [x.strip().split("\n") for x in open("19").read().split("\n\n")]


rules = {}

for rule in inp[0]:
    rule = rule.split("{")
    rn = rule[0]
    crit_raw = rule[1][:-1].split(",")

    crits = []

    for c in crit_raw[:-1]:
        cc = c.strip().split(":")

        ccc = ((cc[0][0], cc[0][1], int(cc[0][2:])), cc[1])
        crits.append(ccc)

    rules[rn] = (crits, crit_raw[-1])

# print(rules)


paths = []
# Find all paths from rule 'in' to rule 'A'

flip_sign = lambda x: "<" if x == ">" else ">"


def find_paths(rule, path):
    if rule == "A":
        paths.append(path)
        return

    if rule == "R":
        return

    cur_rule = rules[rule]
    rules_used = [x[0] for x in cur_rule[0]]
    for i, r in enumerate(cur_rule[0]):
        new_rule = (r[0][0], flip_sign(r[0][1]), r[0][2])
        # Add new rule and the rules that did not fire

        find_paths(r[1], path + [new_rule, *rules_used[:i]])

    find_paths(cur_rule[1], path + rules_used)


find_paths("in", [])

# print(paths)

parts = []

for part in inp[1]:
    content = {}
    part = part.replace("{", "").replace("}", "").split(",")
    for p in part:
        p = p.strip().split("=")
        content[p[0]] = [0, int(p[1]), int(p[1])]
    parts.append(content)

new_parts = []
for part in parts:
    for path in paths:
        new_part = {}
        for k in part:
            new_part[k] = [1, part[k][1], part[k][2]]
        for rule in path:
            if rule[1] == "<":
                new_part[rule[0]][0] += rule[2]
            else:
                new_part[rule[0]][1] = rule[2]

        new_parts.append(new_part)


# Remove parts where one element is 0


total = 0
for part in new_parts:
    part_total = 1
    for k in part:
        # Find range, min of 0 and 2
        # max of 1 and 2
        min_val = min(part[k][0], part[k][1])
        max_val = min(part[k][2], part[k][1])

        # set idx 2 to the number of possible values
        part[k][2] = max(0, max_val - min_val)

    for k in part:
        part_total *= part[k][2]

    total += part_total


new_parts = [x for x in new_parts if not any([x[k][0] > x[k][1] for k in x])]
# print(new_parts)
# # Extract the k[2] values

only = []
for part in new_parts:
    only.append([x[2] for x in part.values()])

ttolt = 0
for part in only:
    total = 1
    for p in part:
        total *= p
        print(total)
    ttolt += total

print(ttolt)
