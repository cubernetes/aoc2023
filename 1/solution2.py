#!/usr/bin/env python3

import re

digit_map = {
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

total = 0
for line in open(0):
    m1 = re.search(r'\d', line)
    m2 = re.search(fr'{"|".join(digit_map)}', line)
    first1 = m1.group(0) if m1 else 'uniquestring'
    first2 = m2.group(0) if m2 else 'uniquestring'
    try:
        i1 = line.index(first1)
    except ValueError:
        i1 = float('inf')
    try:
        i2 = line.index(first2)
    except ValueError:
        i2 = float('inf')
    if i2 < i1:
        first = str(digit_map[first2])
    else:
        first = first1

    rev_line = line[::-1]
    m1 = re.search(r'\d', rev_line)
    m2 = re.search(fr'{"|".join([digit[::-1] for digit in digit_map])}', rev_line)
    last1 = m1.group(0) if m1 else 'uniquestring'
    last2 = m2.group(0) if m2 else 'uniquestring'
    try:
        i1 = rev_line.index(last1)
    except ValueError:
        i1 = float('inf')
    try:
        i2 = rev_line.index(last2)
    except ValueError:
        i2 = float('inf')
    if i2 < i1:
        last = str(digit_map[last2[::-1]])
    else:
        last = last1

    total += int(first + last)

print(total)
