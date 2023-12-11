#!/usr/bin/env python3

import numpy as np

data = open(0).read().strip()
lines = list(map(list, data.splitlines()))

positions = []
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == '#':
            positions.append((r, c))
lines_t = np.transpose(lines)

empties = []
empties_t = []
for r, line in enumerate(lines):
    if set(line) == {'.'}:
        empties.append(r)
for c, line_t in enumerate(lines_t):
    if set(line_t) == {'.'}:
        empties_t.append(c)

distances = 0
for pos in positions:
    for pos_ in positions:
        if pos != pos_:
            r_diff = abs(pos[0] - pos_[0])
            c_diff = abs(pos[1] - pos_[1])
            p = min(pos[0], pos_[0])
            for r in range(p + 1, p + r_diff):
                if r in empties:
                    r_diff += 1_000_000 - 1
            p = min(pos[1], pos_[1])
            for c in range(p + 1, p + c_diff):
                if c in empties_t:
                    c_diff += 1_000_000 - 1
            distances += r_diff + c_diff

print(distances / 2)

# wrong: 82000210

