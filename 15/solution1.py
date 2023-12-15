#!/usr/bin/env python3

data = open(0).read().strip()
parts = data.split(',')

def hash_(s) -> int:
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

t = 0
for part in parts:
    t += hash_(part)

print(t)
