#!/usr/bin/env python3

from math import factorial as fact

def binom(n, k):
    assert type(n) == int and type(k) == int and k >= 0 and n >= 0
    if k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

def backtrack_no(hist: str, runs: list) -> int:
    assert hist and runs
    ridx = 0
    i = 0
    while i < len(hist) and hist[i] != '?':
        i += 1

    q_len = 0
    while i < len(hist) and hist[i] == '?':
        q_len += 1
        i += 1
    tmp_q_len = q_len
    max_fit = 0
    start_ridx = ridx
    while ridx < len(runs) and runs[ridx] <= tmp_q_len:
        last = False
        if ridx == len(runs) - 1 or tmp_q_len - runs[ridx] <= runs[ridx + 1]:
            last = True
        tmp_q_len -= runs[ridx] + (not last)
        ridx += 1
        max_fit += 1
        if last:
            break
    binom(q_len - sum(runs[start_ridx:ridx]) + 1, max_fit)
    return 0

def backtrack_no2(hist: list, runs: list) -> int:
    assert hist and runs
    i = 0
    while i < len(hist) and hist[i] != '?':
        i += 1
    q_len = 0
    while i < len(hist) and hist[i] == '?':
        q_len += 1
        i += 1
    ridx = 0
    print(hist)
    if runs[ridx] < q_len:
        hist[i-q_len:i-q_len+runs[ridx]] = '#' * runs[ridx]
        hist[i-q_len+runs[ridx]:i-q_len+runs[ridx]+1] = '.'
    print(hist)
    return 0

def backtrack(hist: list, runs: list) -> int:
    assert hist and runs
    start_i = 0
    while start_i < len(hist) and hist[start_i] not in '?#':
        start_i += 1
    ridx = 0

    j = start_i
    while j < len(hist) and hist[j] in '?#':
        j += 1

    print(runs)
    tried_i = []
    for i in range(start_i, j):
        if i in tried_i:
            continue
        run_l = 0
        start_j = i
        while i <= j:
            tried_i.append(i)
            j = i
            start_j = i
            run_l = 0
            while j < len(hist) and hist[j] in '?#':
                if run_l == runs[ridx]:
                    break
                j += 1
                run_l += 1
            if run_l != runs[ridx]:
                i += 1
                continue
            if (j < len(hist) and hist[j] == '#') or (start_j > 1 and hist[start_j - 1] == '#'):
                i += 1
                continue
            break
        if run_l == runs[ridx]:
            print(start_j, j)
    ridx += 1
    return 0

total = 0
for line in open(0):
    hist, runs = line.strip().split()
    total += backtrack(list('?'.join([hist] * 1)), list(map(int, runs.split(','))) * 1)

print(total)
