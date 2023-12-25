import numpy as np
from z3 import Int, IntVector, Solver

lines = [x.strip() for x in open("24").readlines()]

# x and y min / max
bounds = (200000000000000, 400000000000000)

hails = []
for l in lines:
    p = l.split(" @ ")
    coords = tuple([int(x) for x in p[0].split(", ")])
    vel = tuple([int(x) for x in p[1].split(", ")])

    hails.append((coords, vel))
points = [x[0] for x in hails]
velocities = [x[1] for x in hails]  # Replace with actual values




# I have no idea how z3 works
# This was jerry rigged from other examples of Z3, my own work for the equations
#   but also biases from the examples probably
# I got many hints for this problem (many of which I didn't understand)
# I do not like math
ns = [(*x[0], *x[1])  for x in hails[:3]]
sp1, sp2, sp3, sv1, sv2, sv3 = IntVector("stone", 6)
ts = IntVector("t", len(ns))
s = Solver()

for t, (hp1, hp2, hp3, hv1, hv2, hv3) in zip(ts, ns):
    s.add(sp1 + t * sv1 == hp1 + t * hv1)
    s.add(sp2 + t * sv2 == hp2 + t * hv2)
    s.add(sp3 + t * sv3 == hp3 + t * hv3)

s.check()
model = s.model()
res = [model[x].as_long() for x in (sp1, sp2, sp3, sv1, sv2, sv3)]
print(res)
print(sum(res[:3]))