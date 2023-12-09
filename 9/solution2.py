#!/usr/bin/env python3

from math import factorial as fact

data = open(0).read().strip()
lines = data.splitlines()

def get_difference_seq(ns):
    ds = []
    for n, next in zip(ns, ns[1:]):
        ds.append(next - n)
    return ds

def get_firsts(ns):
    seqs = [ns]
    while any(seqs[-1]) or len(seqs[-1]) != 1:
        ds = get_difference_seq(seqs[-1])
        seqs.append(ds)
    firsts = []
    for s in seqs:
        firsts.append(s[0])
    return firsts

def binom_with_neg(n, k):
    assert type(n) == int and type(k) == int and k >= 0
    if k > n and n >= 0:
        return 0
    sign = 1
    if n < 0:
        sign = (-1)**k
        n = -n + k - 1
    return int(sign * (fact(n) / (fact(k) * fact(n - k))))

def get_nth(n, firsts):
    s = 0
    for i, f in enumerate(firsts):
        s += f * binom_with_neg(n, i) # gregory-newton interpolation
    return s

t = 0
for line in lines:
    line = list(map(int, line.split()))
    firsts = get_firsts(line)
    t += get_nth(-1, firsts)

print(t)
