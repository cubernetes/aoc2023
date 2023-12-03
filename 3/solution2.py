#!/usr/bin/env python3

import re
import sys
from functools import lru_cache
from collections import deque


data = open(0).read().strip()
lines = data.splitlines()

line_len = len(lines[0])
lines = ['.' * line_len, *lines, '.' * line_len]
total = 0

def get_neighs(line1, line2, line3, i) -> list[int]:
    neighs = []
    l1m = re.finditer(r'\d+', line1)
    l2m = re.finditer(r'\d+', line2)
    l3m = re.finditer(r'\d+', line3)
    for m in l1m:
        start, end = m.span()
        n = int(m.group(0))
        if i in list(range(start - 1, end + 1)):
            neighs.append(n)
            continue
    for m in l3m:
        start, end = m.span()
        n = int(m.group(0))
        if i in list(range(start - 1, end + 1)):
            neighs.append(n)
            continue
    for m in l2m:
        start, end = m.span()
        n = int(m.group(0))
        if i in list(range(start - 1, end + 1)):
            neighs.append(n)
            continue
    return neighs

for line1, line2, line3 in list(zip(lines, lines[1:], lines[2:])):
    for i, s in enumerate(line2):
        if s == '*':
            neighs = get_neighs(line1, line2, line3, i)
            if len(neighs) == 2:
                total += neighs[0] * neighs[1]

print(total)
