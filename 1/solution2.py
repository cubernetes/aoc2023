#!/usr/bin/env python3

import re
from functools import lru_cache
from collections import deque


data = open(0).read().strip()
lines = data.splitlines()
digits_s = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

s = 0
for line in lines:
    m1 = re.search(r'\d', line)
    m2 = re.search(fr'{"|".join(digits_s)}', line)
    first1 = m1.group(0) if m1 else 'xxxxxxxxxxxxxxxxxxxxx'
    first2 = m2.group(0) if m2 else 'xxxxxxxxxxxxxxxxxxxxx'
    try:
        i1 = line.index(first1)
    except ValueError:
        i1 = 99999999
    try:
        i2 = line.index(first2)
    except ValueError:
        i2 = 9999999
    if i2 < i1:
        first = str(digits_s[first2])
    else:
        first = first1

    m1 = re.search(r'\d', line[::-1])
    m2 = re.search(fr'{"|".join([digit_s[::-1] for digit_s in digits_s])}', line[::-1])
    first1 = m1.group(0) if m1 else 'xxxxxxxxxxxxxxxxxxxxx'
    first2 = m2.group(0) if m2 else 'xxxxxxxxxxxxxxxxxxxxx'
    try:
        i1 = line[::-1].index(first1)
    except ValueError:
        i1 = 99999999
    try:
        i2 = line[::-1].index(first2)
    except ValueError:
        i2 = 9999999
    if i2 < i1:
        last = str(digits_s[first2[::-1]])
    else:
        last = first1

    num = int(first + last)
    s += num
print(s)
