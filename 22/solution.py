#!/usr/bin/env python3

print()

import os
import re
import sys
import math
from copy import copy, deepcopy
import numpy as np
import more_itertools as miter
from functools import cache, lru_cache, reduce
from collections import deque, defaultdict, Counter
from itertools import (
    repeat, cycle, combinations, combinations_with_replacement,
    permutations, tee, pairwise, zip_longest, islice, takewhile,
    filterfalse, starmap
)
e=enumerate

data = open(0).read().strip()
lines = data.splitlines()

def vis_x(cubes: list[list[list[int]]]) -> None:
    """
        Minimal values are assumed to be at least 0.
    """
    # initialization
    min_x = float('inf')
    max_x = float(0)
    min_z = float('inf')
    max_z = float(0)
    for cube in cubes:
        (sx, _sy, sz), (ex, _ey, ez) = cube
        min_x = min(min_x, sx, ex)
        max_x = max(max_x, sx, ex)
        min_z = min(min_z, sz, ez)
        max_z = max(max_z, sz, ez)
    if type(min_x) != int or type(max_x) != int or type(min_z) != int or type(max_z) != int:
        assert False

    # rendering
    projection = [[['.', float('inf')] for _ in range(min_x, max_x + 1)] for _ in range(0, max_z)]
    for i, cube in e(cubes):
        (sx, sy, sz), (ex, ey, ez) = cube
        assert ex >= sx and ey >= sy
        for z in range(sz, ez + 1):
            for x in range(sx, ex + 1):
                if sy < projection[z - min_z][x - min_x][1]:
                    projection[z - min_z][x - min_x][0] = chr(((i + 32) % 94 + 33))
                    projection[z - min_z][x - min_x][1] = sy

    # printing
    print(('{:^%ds}' % (max_x - min_x + 1)).format('x'))
    for y in range(min_x, max_x + 1):
        print(end=str(y))
    print()
    for i, line in e(projection[::-1]):
        print(end=''.join(map(lambda tup: tup[0], line)))
        print(end=f' {max_z - i}')
        if i == len(projection) // 2:
            print(' z')
        else:
            print()
    print(f'{"-" * (max_x - min_x + 1)} 0')

def vis_y(cubes: list[list[list[int]]]) -> None:
    """
        Minimal values are assumed to be at least 0.
    """
    # initialization
    min_y = float('inf')
    max_y = float(0)
    min_z = float('inf')
    max_z = float(0)
    for cube in cubes:
        (_sx, sy, sz), (_ex, ey, ez) = cube
        min_y = min(min_y, sy, ey)
        max_y = max(max_y, sy, ey)
        min_z = min(min_z, sz, ez)
        max_z = max(max_z, sz, ez)
    if type(min_y) != int or type(max_y) != int or type(min_z) != int or type(max_z) != int:
        assert False

    # rendering
    projection = [[['.', float('inf')] for _ in range(min_y, max_y + 1)] for _ in range(0, max_z)]
    for i, cube in e(cubes):
        (sx, sy, sz), (ex, ey, ez) = cube
        assert ex >= sx and ey >= sy
        for z in range(sz, ez + 1):
            for y in range(sy, ey + 1):
                if sx < projection[z - min_z][y - min_y][1]:
                    projection[z - min_z][y - min_y][0] = chr(((i + 32) % 94 + 33))
                    projection[z - min_z][y - min_y][1] = sx

    # printing
    print(('{:^%ds}' % (max_y - min_y + 1)).format('y'))
    for y in range(min_y, max_y + 1):
        print(end=str(y))
    print()
    for i, line in e(projection[::-1]):
        print(end=''.join(map(lambda tup: tup[0], line)))
        print(end=f' {max_z - i}')
        if i == len(projection) // 2:
            print(' z')
        else:
            print()
    print(f'{"-" * (max_y - min_y + 1)} 0')

def fall_once(cubes: list[list[list[int]]]) -> list[list[list[int]]]:
    """
        assumes that start z is lower equal end z
    """
    cubes = sorted(cubes, key=lambda cube: cube[0][2])
    new_cubes = []
    for cube in cubes:
        (sx, sy, sz), (ex, ey, ez) = cube
        # print(new_cubes) # DEBUG
        # print(cube) # DEBUG
        # print() # DEBUG
        if sz == 1:
            new_cubes.append(cube)
            continue
        elif not new_cubes:
            new_cubes.append([(sx, sy, sz - 1), (ex, ey, ez - 1)])
            continue
        elif new_cubes[-1][1][2] < sz - 1: # at least one empty z row? Nothing that could stop the fall
            # print('empty row') # DEBUG
            new_cubes.append([(sx, sy, sz - 1), (ex, ey, ez - 1)])
            continue
        new_sz = sz - 1
        new_ez = ez - 1
        can_fall = True
        for below_cube in new_cubes[::-1]:
            (bsx, bsy, bsz), (bex, bey, bez) = below_cube
            if bez > new_sz:
                continue
            if bez == new_sz:
                for x in range(sx, ex + 1):
                    for y in range(sy, ey + 1):
                        # print(f'checking if {x=} is between {bsx=} and {bex=} and') # DEBUG
                        # print(f'checking if {y=} is between {bsy=} and {bey=}') # DEBUG
                        if x in range(bsx, bex + 1) and y in range(bsy, bey + 1):
                            # print('fail') # DEBUG
                            can_fall = False
                            break
                        # print('success') # DEBUG
                        # print() # DEBUG
                    if not can_fall:
                        break
            if not can_fall:
                break
            else:
                break
        if can_fall:
            new_cubes.append([(sx, sy, new_sz), (ex, ey, new_ez)])
        else:
            new_cubes.append([(sx, sy, sz), (ex, ey, ez)])
    return new_cubes

def same_cubes(cubes1: list[list[list[int]]], cubes2: list[list[list[int]]]) -> bool:
    cubes1 = sorted(cubes1, key=lambda cube: cube[0][2])
    cubes2 = sorted(cubes2, key=lambda cube: cube[0][2])
    return cubes1 == cubes2

def simulate_until_rest(cubes: list[list[list[int]]]) -> list[list[list[int]]]:
    prev_cubes = deepcopy(cubes)
    cubes = fall_once(cubes)
    while not same_cubes(cubes, prev_cubes):
        prev_cubes = deepcopy(cubes)
        cubes = fall_once(cubes)
    return cubes

cubes = []
for line in lines:
    start, end = line.split('~')
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))
    cubes.append([start, end])

cubes = simulate_until_rest(cubes)
vis_x(cubes)
vis_y(cubes)
cubes = sorted(cubes, key=lambda cube: cube[0][2], reverse=True)
print(cubes)

supports = set()
max_z = 0
for i, cube in e(cubes):
    (sx, sy, sz), (ex, ey, ez) = cube
    max_z = max(max_z, sz)
    prev_below_cube = None
    sups = 0
    for j, below_cube in e(cubes[i + 1:]):
        (bsx, bsy, bsz), (bex, bey, bez) = below_cube
        break_early = False
        if bez == sz - 1:
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    if x in range(bsx, bex + 1) and y in range(bsy, bey + 1):
                        sups += 1
                        print('before', supports)
                        if sups == 2:
                            print(f'{cube} doubly supported by {below_cube=} and {prev_below_cube=}')
                            print(bez, sz - 1)
                            supports.add(str(below_cube))
                            supports.add(str(prev_below_cube if prev_below_cube is not None else below_cube))
                        if sups > 2:
                            print(f'{cube} {j + 1}-ly supported by {below_cube=}')
                            supports.add(str(below_cube))
                        print('after', supports)
                        prev_below_cube = below_cube
                        break
                if break_early:
                    break
        prev_below_cube = below_cube

print(len(supports) + len(list(filter(lambda cube: cube[0][2] == max_z, cubes)))) # topmost can always be disintegrated
# wrong 65
# wrong 66
