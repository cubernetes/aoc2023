#!/usr/bin/env python3

# import os
# import re
# import sys
# import math
import sympy as syp
import multiprocessing as mp
# from scipy.special import binom
# from copy import copy, deepcopy
from typing import Any
# import numpy as np
# import more_itertools as miter
# from functools import cache, lru_cache, reduce
# from collections import deque, defaultdict, Counter
# from itertools import (
#     repeat, cycle, combinations, combinations_with_replacement,
#     permutations, tee, pairwise, zip_longest, islice, takewhile,
#     filterfalse, starmap
# )
e=enumerate

data = open(0).read().strip().splitlines()

R = len(data)
C = len(data[0])
RANGE_MIN = 200000000000000
RANGE_MAX = 400000000000000

# RANGE_MIN = 7
# RANGE_MAX = 27

x = syp.symbols('x')

def parse_grid(data: list[str]) -> Any:
    for r in range(R):
        for c in range(C):
            pass
def parse_lines(data: list[str]) -> Any:
    hailstones = []
    for line in data:
        p1, p2 = line.split('@')
        px, py, pz = map(int, p1.split(', '))
        vx, vy, vz = map(int, p2.split(', '))
        hailstones.append((vy / vx * x + py - (vy / vx * px), (px, py, pz, vx, vy, vz)))
    return hailstones

def parse_line(data: list[str]) -> Any:
    return data[0].split()
# data = parse_line(data)
# data = parse_grid(data)
hailstones = parse_lines(data)

def intersections(start, end, ret):
    global hailstones
    if start not in ret:
        ret[start] = 0
    print(start, end)
    n = start
    t = 0
    # N = int(binom(len(hailstones), 2))
    for i, (stone_a, stuff_a) in e(hailstones[start:end]):
        for (stone_b, stuff_b) in hailstones[start+i+1:]:
            # n += 1
            # print(n, ' ', N)
            # print(n)
            inter_xs = syp.solve(stone_a - stone_b, x)
            if len(inter_xs) == 1:
                inter_x = inter_xs[0]
                inter_y = stone_a.subs(x, inter_x)
                if (
                    RANGE_MIN <= inter_x <= RANGE_MAX \
                    and RANGE_MIN <= inter_y <= RANGE_MAX \
                    and ((stuff_a[3] < 0 and inter_x <= stuff_a[0]) \
                    or (stuff_a[3] >= 0 and inter_x >= stuff_a[0])) \
                    and ((stuff_b[3] < 0 and inter_x <= stuff_b[0]) \
                    or (stuff_b[3] >= 0 and inter_x >= stuff_b[0]))
                ):
                    t += 1
                else:
                    pass # outside/crosses in the past
            elif len(inter_xs) == 0:
                pass # parallel
            else:
                assert False, inter_xs # same line
    ret[start] = t

if __name__ == '__main__':
    procs = []
    N = 12
    i = 0
    manager = mp.Manager()
    ret = manager.dict()
    while i < N:
        p = mp.Process(target=intersections,
                        args=(i * len(hailstones) // N, (i+1) * len(hailstones) // N, ret))
        procs.append(p)
        p.start()
        i += 1
    for proc in procs:
        proc.join()
    print('Crossings:', sum(ret.values()))

# too low: 2739
# too low: 2774
# too high: 32047
