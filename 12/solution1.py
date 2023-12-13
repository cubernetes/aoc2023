#!/usr/bin/env python3

import re

data = open(0).read().strip()
lines = data.splitlines()

total = 0
def gen_possibilities(hist, pattern) -> None:
    global total

    i = 0
    while i < len(hist) and hist[i] != '?':
        i += 1
    if i == len(hist):
        if pattern.match(''.join(hist)):
            total += 1
        return
    gen_possibilities(hist[:i] + ['.'] + hist[i + 1:], pattern)
    gen_possibilities(hist[:i] + ['#'] + hist[i + 1:], pattern)

for line in lines:
    line = line.split()
    hist, runs = line
    hist = list(hist)
    runs = list(map(int, runs.split(',')))
    s_pattern = r'\.*'
    for i, run in enumerate(runs):
        if i > 0:
            s_pattern += r'\.+'
        s_pattern += r'#{' + str(run) + '}'
    s_pattern += r'\.*$'
    pattern = re.compile(s_pattern)
    gen_possibilities(hist, pattern)
    print(total)
print(total)
