#!/usr/bin/env python3

import re
import sys
from functools import lru_cache
from collections import deque


data = open(0).read().strip()
lines = data.splitlines()

s = 0 
red, green, blue = 12, 13, 14
for i, line in enumerate(lines):
    def one_pass(line: str) -> bool:
        line = re.sub(r'Game \d+: ', '', line)
        sets_of_cubes = line.split('; ')
        for set_ in sets_of_cubes:
            set_of_cubes = set_.split(', ')
            for selection in set_of_cubes:
                amount, color = selection.split(' ')
                amount = int(amount)
                if color == 'red':
                    if amount > red:
                        return False
                if color == 'green':
                    if amount > green:
                        return False
                if color == 'blue':
                    if amount > blue:
                        return False
        return True
    if one_pass(line):
        s += i + 1

print(s)
