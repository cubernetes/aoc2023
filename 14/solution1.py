#!/usr/bin/env python3

grid = list(map(list, open(0).read().strip().splitlines()))
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'O':
            for up in range(r - 1, -1, -1):
                if grid[up][c] == '.':
                    grid[up+1][c] = '.'
                    grid[up][c] = 'O'
                else:
                    break

load = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'O':
            load += len(grid) - r

print(load)
