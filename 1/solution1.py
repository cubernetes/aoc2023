#!/usr/bin/env python3

import re

total = 0
for line in open(0):
    m = re.search(r'\d', line)
    first = m.group(0) if m else ''

    m = re.search(r'\d', line[::-1])
    last = m.group(0) if m else ''

    total += int(first + last) if first + last else 0

print(total)
