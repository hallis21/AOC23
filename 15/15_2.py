cmds = open("15_2").read().strip().split(",")


def hash(cmd):
    t = [ord(x) for x in cmd]
    # [
    #     t.__setitem__(0, ((t[i] + t[0]) * 17) % 256)
    #     for i in [0]+list(range(len(t))) if i != 0
    # ]

    cur_hash = 0
    for i in range(len(t)):
        cur_hash = (cur_hash + t[i]) * 17 % 256

    return cur_hash


boxes = {}

for cmd in cmds:
    if "=" in cmd:
        pos, val = cmd.split("=")
        h = hash(pos)
        if h not in boxes:
            boxes[h] = {pos: val}
        else:
            boxes[h][pos] = val
    if "-" in cmd:
        pos = cmd[:-1]
        h = hash(pos)
        if h in boxes:
            if pos in boxes[h]:
                del boxes[h][pos]
                if len(boxes[h]) == 0:
                    del boxes[h]
    

sum_focal = 0


for box in boxes:
    if len(boxes[box]) >= 255:
        print(box)
    for i,pos in enumerate(boxes[box].values()):
        sum_focal += (1+box)*(i+1)*int(pos)
print(sum_focal)