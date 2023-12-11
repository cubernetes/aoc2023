#!/usr/bin/env python3

import numpy as np

data = open(0).read().strip()
lines__ = list(map(list, data.splitlines()))

lines_ = []
for line in lines__:
    if set(line) == {'.'}:
        lines_.append(line)
        lines_.append(line)
    else:
        lines_.append(line)
lines_ = np.transpose(lines_)

lines = []
for line in lines_:
    if set(line) == {'.'}:
        lines.append(line)
        lines.append(line)
    else:
        lines.append(line)
lines = np.transpose(lines)

galaxies = []
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == '#':
            galaxies.append((r, c))

distances = 0
for galaxy_a in galaxies:
    for galaxy_b in galaxies:
        if galaxy_a != galaxy_b:
            r_diff = abs(galaxy_a[0] - galaxy_b[0])
            c_diff = abs(galaxy_a[1] - galaxy_b[1])
            distances += r_diff + c_diff

print(distances / 2)
