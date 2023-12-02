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
    def one_pass(line: str) -> int:
        max_red = max_green = max_blue = -1
        line = re.sub(r'Game \d+: ', '', line)
        sets_of_cubes = line.split('; ')
        for set_ in sets_of_cubes:
            set_of_cubes = set_.split(', ')
            for selection in set_of_cubes:
                amount, color = selection.split(' ')
                amount = int(amount)
                if color == 'red':
                    if amount > max_red:
                        max_red = amount
                if color == 'green':
                    if amount > max_green:
                        max_green = amount
                if color == 'blue':
                    if amount > max_blue:
                        max_blue = amount
        power = max_red * max_green * max_blue
        return power
    power = one_pass(line)
    s += power

print(s)
