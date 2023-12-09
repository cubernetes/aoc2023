#!/usr/bin/env python3

import scipy.special

data = open(0).read().strip()
lines = data.splitlines()

def difference_seq(ns):
    ds = []
    for n, next in zip(ns, ns[1:]):
        ds.append(next - n)
    return ds

def get_firsts(ns):
    seqs = [ns]
    while any(seqs[-1]):
        ds = difference_seq(seqs[-1])
        seqs.append(ds)
    firsts = []
    for s in seqs:
        firsts.append(s[0])
    return firsts

def binom(x, y):
    if x < 0:
        return (-1)**y * int(scipy.special.binom(-x + y - 1, y))
    return int(scipy.special.binom(x, y))

def get_n(n, firsts):
    s = 0
    for i, f in enumerate(firsts):
        s += f * binom(n, i)
    return s

t = 0
for line in lines:
    line = list(map(int, line.split()))
    firsts = get_firsts(line)
    t += get_n(len(line), firsts)

print(t)
