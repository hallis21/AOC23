from collections import defaultdict


lines = [x.strip().split(" -> ") for x in open("20").readlines()]

network = {}
cons = []
for l in lines:
    if l[0] == "broadcaster":
        network[l[0]] = [x for x in l[1].split(", ")]
    if l[0][0] == "%":
        network[l[0][1:]] = (False, [[x for x in l[1].split(", ")], False])
    if l[0][0] == "&":
        network[l[0][1:]] = (True, [[x for x in l[1].split(", ")], {}])
        cons.append(l[0][1:])
    
for key in network.keys():
    n = []
    if key == "broadcaster":
        n = network[key]
    else:
        n = network[key][1][0]


    for connector in n:
        if connector in cons:
            network[connector][1][1][key] = False




node_names = network.keys()
# print(network)
# exit()
# (dest, true/false) 
pulses = []

def handle_pulse(node, t, sender, i):
    n = network[node]
    if node == "broadcaster":
        [pulses.append((d, False, "broadcaster")) for d in network['broadcaster']]
        return
    keys = n[1][0]
    if not t and not n[0]:
        n[1][1] = not n[1][1]
        [pulses.append((d, n[1][1], node)) for d in keys]

    elif n[0]:
        n[1][1][sender] = t

        if all(n[1][1].values()):
            [pulses.append((d, False, node)) for d in keys]
            if "vr" in keys:
                print("FOUND RX AT:", i)
                exit()

        else:
            [pulses.append((d, True, node)) for d in keys]

def button():
    pulses.append(("broadcaster", False,"butt"))



low = 0
high = 0

iter = 0
while True:
    iter += 1
    button()
    # print()
    while len(pulses) > 0:
        pulse = pulses.pop(0)
        # print(pulse[-1], "-high->" if pulse[1] else "-low->", pulse[0])

        if pulse[1]:
            high += 1
        else:
            low += 1
        
        if pulse[0] in node_names:
            handle_pulse(pulse[0], pulse[1], pulse[2], iter)

print(high, low, (high)*(low))