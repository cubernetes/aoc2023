#!/usr/bin/env python3

from collections import defaultdict
e=enumerate

parts = open(0).read().strip().split(',')

def hash_(s) -> int:
    v = 0
    for c in label:
        v += ord(c)
        v *= 17
        v %= 256
    return v
t = 0
hashmap = defaultdict(list)
for part in parts:
    if '-' in part:
        label = part.removesuffix('-')
        h = hash_(label)
        for i, (l, f) in e(hashmap[h]):
            if l == label:
                del hashmap[h][i]
                break
    elif '=' in part:
        label, focal_len = part.split('=')
        h = hash_(label)
        found = False
        for i, (l, f) in e(hashmap[h]):
            if l == label:
                found = True
                hashmap[h][i] = (label, int(focal_len))
                break
        if not found:
            hashmap[h].append((label, int(focal_len)))
    else:
        assert False

t = 0
for box_number, lenses in hashmap.items():
    for i, (label, focal_len) in e(lenses):
        s = (1 + box_number)
        s *= i + 1
        s *= focal_len
        t += s

print(t)
