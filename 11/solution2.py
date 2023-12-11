#!/usr/bin/env python3

import numpy as np

data = open(0).read().strip()
lines = list(map(list, data.splitlines()))
lines_t = np.transpose(lines)

galaxies = []
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == '#':
            galaxies.append((r, c))

empties = []
empties_t = []
for r, line in enumerate(lines):
    if set(line) == {'.'}:
        empties.append(r)
for c, line_t in enumerate(lines_t):
    if set(line_t) == {'.'}:
        empties_t.append(c)

factor = 1_000_000
distances = 0
for galaxy_a in galaxies:
    for galaxy_b in galaxies:
        if galaxy_a != galaxy_b:
            r_diff = abs(galaxy_a[0] - galaxy_b[0])
            c_diff = abs(galaxy_a[1] - galaxy_b[1])

            r_start = min(galaxy_a[0], galaxy_b[0])
            for r in range(r_start + 1, r_start + r_diff):
                if r in empties:
                    r_diff += factor - 1

            c_start = min(galaxy_a[1], galaxy_b[1])
            for c in range(c_start + 1, c_start + c_diff):
                if c in empties_t:
                    c_diff += factor - 1

            distances += r_diff + c_diff

print(distances / 2)
