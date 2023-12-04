#!/usr/bin/env python3

import re
import sys
from functools import lru_cache
from collections import deque, defaultdict


data = open(0).read().strip()
lines = data.splitlines()

t = 0
for line in lines:
    winning, my = line.split(":")[1].split('|')
    winning = winning.split()
    my = my.split()
    n = set(my) & set(winning)
    n = len(n)
    if n > 0:
        s = 2 ** (n - 1)
        t += s

print(t)
