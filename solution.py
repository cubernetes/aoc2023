#!/usr/bin/env python3

import re
from functools import lru_cache
from collections import deque


data = open(0).read().strip()
lines = data.splitlines()

s = 0
for line in lines:
    m = re.search(r'\d', line)
    first = m.group(0)
    m = re.search(r'\d', line[::-1])
    last = m.group(0)
    num = int(first + last)
    s += num
print(s)
