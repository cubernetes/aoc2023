#!/usr/bin/env python3

import numpy as np

patterns = open(0).read().split('\n\n')

t = 0
for i, pattern in enumerate(patterns):
    pattern = np.array([list(line) for line in pattern.splitlines()])
    for row in range(len(pattern) - 1):
        up = row
        down = row + 1
        j = 0
        err = 0
        while up - j >= 0 and down + j < len(pattern):
            for a, b in zip(pattern[up - j], pattern[down + j]):
                if a != b:
                    err += 1
            j += 1
        if err == 0:
            t += (row + 1) * 100
    pattern = np.transpose(pattern)
    for column in range(len(pattern) - 1):
        up = column
        down = column + 1
        j = 0
        err = 0
        while up - j >= 0 and down + j < len(pattern):
            for a, b in zip(pattern[up - j], pattern[down + j]):
                if a != b:
                    err += 1
            j += 1
        if err == 0:
            t += column + 1

print(t)
