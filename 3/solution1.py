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
for line1, line2, line3 in list(zip(lines, lines[1:], lines[2:])):
    def one_pass(line1: str, line2: str, line3: str) -> int:
        def inside_pass(line1: str, line2: str, match, line3: str) -> int:
            start, end = match.span()
            n = int(match.group(0))
            for s in line1[max(0, start - 1) : min(line_len - 1, end + 1)]:
                if s != '.':
                    return n
            for s in line3[max(0, start - 1) : min(line_len - 1, end + 1)]:
                if s != '.':
                    return n
            if (start > 0 and line2[start - 1] != '.') or (end < line_len and line2[end] != '.'):
                return n
            return 0
        tmp_n = 0
        for match in re.finditer(r'\d+', line2):
            tmp_n += inside_pass(line1, line2, match, line3)
        return tmp_n
    x = one_pass(line1, line2, line3)
    total += x

print(total)
