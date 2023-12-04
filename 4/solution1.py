#!/usr/bin/env python3

total = 0
for line in open(0):
    winning_nums, my_nums = map(set, map(str.split, line.split(":")[1].split('|')))
    n_matching_nums = len(my_nums & winning_nums)
    if n_matching_nums:
        total += 2 ** (n_matching_nums - 1)

print(total)
