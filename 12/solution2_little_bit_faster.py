#!/usr/bin/env python3

import re

data = open(0).read().strip()
lines = data.splitlines()

def check(hist: list, runs: list) -> bool:
    i = -1
    broken_len = 0
    runs_idx = 0
    while (i := i + 1) < len(hist):
        if hist[i] == '.':
            if broken_len > 0:
                if runs_idx >= len(runs) or runs[runs_idx] != broken_len:
                    return False
                runs_idx += 1
            broken_len = 0
            continue
        broken_len += 1
    if runs_idx < len(runs) and runs[runs_idx] != broken_len:
        return False
    if hist[-1] == '#':
        runs_idx += 1
    if runs_idx == len(runs):
        return True
    return False

hash_groups = re.compile(r'#+(?![\?#])')

def satisfiable(hist, runs) -> bool:
    global hash_groups

    hist = ''.join(hist)
    hist_split = hist.split('?', 1)
    if len(hist_split) == 2:
        hist = hist_split[0] + '?'
    else:
        hist =  hist_split[0]
    matches = list(map(lambda m: len(m.group()), hash_groups.finditer(hist)))
    for a, b in zip(matches, runs):
        if a != b:
            return False
    return True

branched_killed = []
def gen_possibilities(hist: list, runs: list) -> int:
    if not satisfiable(hist, runs):
        branched_killed[-1] += 1
        return 0
    i = 0
    while i < len(hist) and hist[i] != '?':
        i += 1
    if i == len(hist):
        if check(hist, runs):
            return 1
        return 0
    s = 0
    hist[i] = '.'
    s += gen_possibilities(hist.copy(), runs)
    hist[i] = '#'
    s += gen_possibilities(hist, runs)
    return s

total = 0
for idx, line in enumerate(lines):
    print(branched_killed)
    branched_killed.append(0)
    line = line.split()
    # hist, runs = line
    # hist = list('?'.join([hist] * 1))
    # runs = list(map(int, runs.split(','))) * 1
    # one = gen_possibilities(hist, runs)

    hist, runs = line
    hist = list('?'.join([hist] * 5))
    runs = list(map(int, runs.split(','))) * 5
    two = gen_possibilities(hist, runs)
    # factor = two / one
    # if two % one != 0:
    #     print(line, two, one, factor)
    #     assert False
    # total += one * factor ** 4
    total += two
    print(f'{idx+1}/{len(lines)}')
print(total)
