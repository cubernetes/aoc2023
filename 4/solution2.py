#!/usr/bin/env python3

from collections import defaultdict

cards = defaultdict(lambda: 1)
for i, line in enumerate(open(0)):
    winning_nums, my_nums = map(set, map(str.split, line.split(":")[1].split('|')))
    matching_nums = my_nums & winning_nums
    for j in range(len(matching_nums)):
        cards[i + j + 1] += cards[i]
    cards[i]

print(sum(cards.values()))
