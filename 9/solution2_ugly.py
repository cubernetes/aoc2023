#!/usr/bin/env python3

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

def get_prev(n, firsts):
    rev = firsts[::-1]
    x = rev[0]
    for r in rev[1:-1]:
        print(x)
        x = r - x
    print(x)
    print(n - x)
    print()
    return n - x

t = 0
for line in lines:
    line = list(map(int, line.split()))
    firsts = get_firsts(line)
    t += get_prev(line[0], firsts)

print(t)
