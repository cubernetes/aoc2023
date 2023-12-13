#!/usr/bin/env python3

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

def gen_possibilities(hist: list, runs: list) -> int:
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
    line = line.split()
    hist, runs = line
    hist = list('?'.join([hist] * 1))
    runs = list(map(int, runs.split(','))) * 1
    one = gen_possibilities(hist, runs)

    hist, runs = line
    hist = list('?'.join([hist] * 2))
    runs = list(map(int, runs.split(','))) * 2
    two = gen_possibilities(hist, runs)
    factor = two / one
    total += one * factor ** 4
    print(f'{idx+1}/{len(lines)}')
print(total)
