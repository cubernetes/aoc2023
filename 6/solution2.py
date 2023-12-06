#!/usr/bin/env python3

data = open(0).read().strip()
lines = data.splitlines()

time = int(lines[0].split(':')[1].strip().replace(' ', ''))
distance = int(lines[1].split(':')[1].strip().replace(' ', ''))

ways = 0
for i in range(time + 1):
    d = i * (time - i)
    if d > distance:
        ways += 1
print(ways)
