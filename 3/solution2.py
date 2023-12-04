#!/usr/bin/env python3

import re

data = open(0).read().strip()
lines = data.splitlines()

line_len = len(lines[0])
lines = ['.'*line_len, *lines, '.'*line_len]
for i, line in enumerate(lines):
    lines[i] = '.' + line + '.'

total = 0
for line1, line2, line3 in list(zip(lines, lines[1:], lines[2:])):
    for i, s in enumerate(line2):
        def get_neighs() -> list[int]:
            neighs = []
            line1_matches = list(re.finditer(r'\d+', line1))
            line2_matches = list(re.finditer(r'\d+', line2))
            line3_matches = list(re.finditer(r'\d+', line3))
            matches = line1_matches + line2_matches + line3_matches
            for m in matches:
                start, end = m.span()
                num = int(m.group(0))
                if i in range(start - 1, end + 1):
                    neighs.append(num)
                    continue
            return neighs
        if s == '*' and len(neighs := get_neighs()) == 2:
            total += neighs[0] * neighs[1]

print(total)
