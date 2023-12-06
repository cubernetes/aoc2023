#!/usr/bin/env python3

data = open(0).read().strip()
lines = data.splitlines()

times = list(map(int, lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))
total = 1
for time, distance in zip(times, distances):
    ways = 0
    for i in range(time + 1):
        d = i * (time - i)
        if d > distance:
            ways += 1
    total *= ways
print(total)
