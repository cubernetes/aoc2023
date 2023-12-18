#!/usr/bin/env python3

import numpy as np

# shoelace formula https://stackoverflow.com/a/30408825
def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
clrs = [(int((a := line.strip().split()[-1][2:-1])[:-1], 16), dirs[int(a[-1:])]) for line in open(0)]

x = y = perim = 0
xs, ys = [], []
for clr in clrs:
    d, (dy, dx) = clr
    xs.append(x := x + dx * d)
    ys.append(y := y + dy * d)
    perim += d

# idk but (perimeter / 2 + 1) somehow works for the border
print(perim / 2 + 1 + PolyArea(xs,ys))
