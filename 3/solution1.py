#!/usr/bin/env python3

import re

data = open(0).read().strip()
lines = data.splitlines()

line_len = len(lines[0])
lines = ['.'*line_len, *lines, '.'*line_len]
for i, line in enumerate(lines):
    lines[i] = '.' + line + '.'

total = 0
for line1, line2, line3 in zip(lines, lines[1:], lines[2:]):
    def is_part_number(match: re.Match) -> bool:
        start, end = match.span()
        if line2[start-1] != '.' or line2[end] != '.':
            return True
        for c in line1[start-1:end+1] + line3[start-1:end+1]:
            if c != '.': return True
        return False

    for match in re.finditer(r'\d+', line2):
        total += int(match.group(0)) if is_part_number(match) else 0

print(total)
