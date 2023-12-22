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

# For every item in queue check the "RULE" and apply it
# Split it so one side gest the rule and the other side gets the inverse 
# ('rule_name', {x: (start, end), m: (start, end) ...})

queue = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]

accepted = []


while len(queue) > 0:
    item = queue.pop(0)

    if item[0] == "A":
        accepted.append(item[1])
        continue
    if item[0] == "R":
        continue

    rule = rules[item[0]]
    part = item[1]
    new_parts = []

    for split in rule[0]:
        cur_part = part.copy()
        part_value = cur_part[split[0][0]]
        new_part_value = cur_part[split[0][0]]
        sign = split[0][1]
        value = split[0][2]
        if sign == ">":
            # The new range should start from the next integer greater than value
            new_part_value = (value + 1, new_part_value[1])
            part_value = (part_value[0], value)
        else:
            # The new range should end at the integer less than value
            new_part_value = (new_part_value[0], value - 1)
            part_value = (value, part_value[1])

        # Append the new part with the rule route (route, part)
        cur_part[split[0][0]] = new_part_value
        part[split[0][0]] = part_value
        new_parts.append((split[1], cur_part))

    # Append the "part" to the final rule
    new_parts.append((rule[1], part))

    queue.extend(new_parts)


all_total = 0
for part in accepted:
    total = 1
    for k in part:
        total *= (part[k][1] - part[k][0] +1)
    all_total += total

print(all_total)




167409079868000
167409079868000
167505012066000
167459205617600