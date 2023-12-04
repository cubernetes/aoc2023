#!/usr/bin/env python3

import re
import sys
from functools import lru_cache
from collections import deque, defaultdict


data = open(0).read().strip()
lines = data.splitlines()

card_multipliers = defaultdict(lambda:1)
total = 0
for i, line in enumerate(lines):
    winning, my = line.split(":")[1].split('|')
    winning = set(winning.split())
    my = set(my.split())
    my_winning = my & winning
    n = len(my_winning)
    for j in range(n):
        card_multipliers[i + j + 2] += card_multipliers[i + 1]
    total += card_multipliers[i + 1]

print(total)
