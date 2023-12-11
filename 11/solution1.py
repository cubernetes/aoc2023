#!/usr/bin/env python3

import re
import sys
import math
import numpy as np
from functools import lru_cache
from collections import deque, defaultdict, Counter


data = open(0).read().strip()
lines__ = data.splitlines()

lines_ = []
for line in lines__:
    if set(line) == {'.'}:
        lines_.append(list(line))
        lines_.append(list(line))
    else:
        lines_.append(list(line))
lines_ = np.transpose(lines_)

lines = []
for line in lines_:
    if set(line) == {'.'}:
        lines.append(list(line))
        lines.append(list(line))
    else:
        lines.append(list(line))
lines = np.transpose(lines)

positions = []
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == '#':
            positions.append((r, c))

distances = 0
for pos in positions:
    for pos_ in positions:
        if pos != pos_:
            r_diff = abs(pos[0] - pos_[0])
            c_diff = abs(pos[1] - pos_[1])
            distances += r_diff + c_diff

print(distances / 2)
