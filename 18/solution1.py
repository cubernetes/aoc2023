#!/usr/bin/env python3

data = open(0).read().strip()
lines = data.splitlines()

r, c = 0, 0
min_r, max_r, min_c, max_c = 0, 0, 0, 0
border = [(r, c)]
for line in lines:
    dir, meters, clr = line.split()
    meters = int(meters)
    clr = clr[1:-1]
    if dir == 'U':
        for m in range(meters):
            r -= 1
            min_r = min(min_r, r)
            border.append((r, c))
    elif dir == 'R':
        for m in range(meters):
            c += 1
            max_c = max(max_c, c)
            border.append((r, c))
    elif dir == 'D':
        for m in range(meters):
            r += 1
            max_r = max(max_r, r)
            border.append((r, c))
    elif dir == 'L':
        for m in range(meters):
            c -= 1
            min_c = min(min_c, c)
            border.append((r, c))

min_r -= 1
max_r += 1
min_c -= 1
max_c += 1
n_inside = 0
border_grid = [['.' for _ in range(max_c - min_c + 1)] for _ in range(max_r - min_r + 1)]
grid = [['.' for _ in range(max_c - min_c + 1)] for _ in range(max_r - min_r + 1)]
for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
        if (r, c) in border:
            border_grid[r - min_r][c - min_c] = '#'
for r in range(min_r + 1, max_r):
    print(r, max_r)
    for c in range(min_c + 1, max_c):
        crossings = 0
        right_ups = []
        down_rights = []
        if (r, c) not in border:
            for i in range(c, max_c + 1):
                if border_grid[r - min_r][i - min_c] == '#':
                    if border_grid[r + 1 - min_r][i - min_c] == '.' and border_grid[r - 1 - min_r][i - min_c] == '.':
                        pass # not a crossing
                    elif border_grid[r - 1 - min_r][i - min_c] == '#' and border_grid[r + 1 - min_r][i - min_c] == '#':
                        crossings += 1
                    elif border_grid[r - 1 - min_r][i - min_c] == '#' and border_grid[r - min_r][i + 1 - min_c] == '#':
                        if right_ups and right_ups[-1] == 'right-up':
                            right_ups.pop()
                            crossings += 1
                        else:
                            right_ups.append('up-right')
                    elif border_grid[r + 1 - min_r][i - min_c] == '#' and border_grid[r - min_r][i - 1 - min_c] == '#':
                        if right_ups and right_ups[-1] == 'up-right':
                            right_ups.pop()
                            crossings += 1
                        else:
                            right_ups.append('right-up')
                    elif border_grid[r + 1 - min_r][i - min_c] == '#' and border_grid[r - min_r][i + 1 - min_c] == '#':
                        if down_rights and down_rights[-1] == 'right-down':
                            down_rights.pop()
                            crossings += 1
                        else:
                            down_rights.append('down-right')
                    elif border_grid[r - 1 - min_r][i - min_c] == '#' and border_grid[r - min_r][i - 1 - min_c] == '#':
                        if down_rights and down_rights[-1] == 'down-right':
                            down_rights.pop()
                            crossings += 1
                        else:
                            down_rights.append('right-down')
            if crossings % 2 == 1:
                grid[r - min_r][c - min_c] = '#'
                n_inside += 1
        else:
            grid[r - min_r][c - min_c] = '#'
            n_inside += 1

# for line in grid:
#     print(''.join(line))
print(n_inside)
