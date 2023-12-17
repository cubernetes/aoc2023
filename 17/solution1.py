#!/usr/bin/env python3

import os
from collections import deque
e=enumerate


DEBUG = False
COLOR = True
data = open(0).read().strip()
lines = data.splitlines()
grid = [list(map(int, line)) for line in lines]
R = len(grid)
C = len(grid[0])
MAX_STRAIGHT = 3
MIN_STRAIGHT = 1

directions = ['e', 'w', 'n', 's']
dp = [[[{dir: float('inf') for dir in directions} for _ in range(MAX_STRAIGHT)] for _ in range(C)] for _ in range(R)]

for block in range(MAX_STRAIGHT):
    for dir in dp[0][0][block]:
        dp[0][0][block][dir] = 0

def print_dp(dp, r_, c_, debug=DEBUG, interactive=True, color=COLOR, path=None):
    return
    if not debug:
        return
    lens = []
    for c in range(C):
        big = 0
        for r in range(R):
            big = max(big, len(''.join([str(val if val != float('inf') else '0')+(dir if dir != 'all' else '?') for val,dir in dp[r][c]])))
        lens.append(big)
    for r in range(R):
        for c in range(C):
            if c > 0:
                print(end=' ')
            print(end=' ' * (lens[c] - len(''.join([str(val if val != float('inf') else '0')+(dir if dir != 'all' else '?') for val,dir in dp[r][c]]))))
            if r == r_ and c == c_:
                if color:
                    print(end='\033\x5b1;4m')
            if path and (r, c) in path:
                if color:
                    print(end='\033\x5b1;4m')
            for j, (val, dir) in e(dp[r][c]):
                if val == float('inf'):
                    val = '∞'
                if dir == 'all':
                    dir = '?'
                if color:
                    print(end=f'\033\x5b3{j+1}m')
                print(end=f'{val}{dir}')
            if color:
                print(end='\033\x5b37m')
            print(end=f'{grid[r][c]}')
            if color:
                print(end='\033\x5bm')
        print()
    if interactive:
        input()
    if DEBUG:
        os.system('clear')

i = 0
while True:
    changed = False
    for r in range(R):
        for c in range(C):
            print_dp(dp, r, c, debug=DEBUG)
            for block in range(MAX_STRAIGHT):
                for dir in directions:
                    val = dp[r][c][block][dir]
                    if c < C - 1:
                        m = val + grid[r][c+1]
                        if dir == 'e':
                            if block < MAX_STRAIGHT - 1 and m < dp[r][c+1][block+1]['e']:
                                dp[r][c+1][block+1]['e'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir in ['n', 's']:
                            if m < dp[r][c+1][0]['e'] and block > MIN_STRAIGHT - 2:
                                dp[r][c+1][0]['e'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir == 'w':
                            pass
                        else:
                            assert False
                    if r < R - 1:
                        m = val + grid[r+1][c]
                        if dir == 's':
                            if block < MAX_STRAIGHT - 1 and m < dp[r+1][c][block+1]['s']:
                                dp[r+1][c][block+1]['s'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir in ['e', 'w']:
                            if m < dp[r+1][c][0]['s'] and block > MIN_STRAIGHT - 2:
                                dp[r+1][c][0]['s'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir == 'n':
                            pass
                        else:
                            assert False
                    if r > 0:
                        m = val + grid[r-1][c]
                        if dir == 'n':
                            if block < MAX_STRAIGHT - 1 and m < dp[r-1][c][block+1]['n']:
                                dp[r-1][c][block+1]['n'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir in ['e', 'w']:
                            if m < dp[r-1][c][0]['n'] and block > MIN_STRAIGHT - 2:
                                dp[r-1][c][0]['n'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir == 's':
                            pass
                        else:
                            assert False
                    if c > 0:
                        m = val + grid[r][c-1]
                        if dir == 'w':
                            if block < MAX_STRAIGHT - 1 and m < dp[r][c-1][block+1]['w']:
                                dp[r][c-1][block+1]['w'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir in ['n', 's']:
                            if m < dp[r][c-1][0]['w'] and block > MIN_STRAIGHT - 2:
                                dp[r][c-1][0]['w'] = m
                                changed = True
                                print_dp(dp, r, c, debug=DEBUG)
                        elif dir == 'e':
                            pass
                        else:
                            assert False
    i += 1
    if not changed:
        break

reached_end = False
for block in dp[R - 1][C - 1]:
    for dir in directions:
        if block[dir] != float('inf'):
            reached_end = True
assert reached_end

def get_path(min_block, min_dir) -> deque:
    prev = (R - 1, C - 1, min_block, min_dir)
    prev_dir = ''
    path = deque()
    while prev[:2] != (0, 0):
        r, c, min_block, dir = prev
        path.appendleft((r, c))
        val = dp[r][c][min_block][dir]
        if dir == 's':
            assert r > 0
            if min_block > 0:
                prev = (r - 1, c, min_block - 1, dir)
            else:
                old_val = val - grid[r][c]
                for i, cand in enumerate(dp[r-1][c]):
                    for dir_ in directions:
                        if cand[dir_] == old_val and dir_ not in ['s', 'n']:
                            prev = (r - 1, c, i, dir_)
                            break
        elif dir == 'n':
            assert r < R - 1
            if min_block > 0:
                prev = (r + 1, c, min_block - 1, dir)
            else:
                old_val = val - grid[r][c]
                for i, cand in enumerate(dp[r+1][c]):
                    for dir_ in directions:
                        if cand[dir_] == old_val and dir_ not in ['n', 's']:
                            prev = (r + 1, c, i, dir_)
                            break
        elif dir == 'e':
            assert c > 0
            if min_block > 0:
                prev = (r, c - 1, min_block - 1, dir)
            else:
                old_val = val - grid[r][c]
                for i, cand in enumerate(dp[r][c-1]):
                    for dir_ in directions:
                        if cand[dir_] == old_val and dir_ not in ['e', 'w']:
                            prev = (r, c - 1, i, dir_)
                            break
        elif dir == 'w':
            assert c < C - 1
            if min_block > 0:
                prev = (r, c + 1, min_block - 1, dir)
            else:
                old_val = val - grid[r][c]
                for i, cand in enumerate(dp[r][c+1]):
                    for dir_ in directions:
                        if cand[dir_] == old_val and dir_ not in ['w', 'e']:
                            prev = (r, c + 1, i, dir_)
                            break
    path.appendleft((0, 0))
    # print((0, 0, -1))
    return path

def get_shortest_line(path: deque) -> int | float:
    if not path:
        return 0

    shortest = float('inf')
    r, c = path.popleft()
    pr, pc = r, c

    while path:
        nr, nc = path.popleft()
        if abs(nr - r) == 0 or abs(nc - c) == 0:
            pass
        else:
            shortest = min(shortest, abs(pr - r) + abs(pc - c) + 1)
            r, c = nr, nc
        pr, pc = nr, nc
    shortest = min(shortest, abs(pr - r) + abs(pc - c) + 1)
    return shortest

valid_paths = []
for min_block in range(MAX_STRAIGHT):
    for min_dir in directions:
        if dp[R - 1][C - 1][min_block][min_dir] == float('inf'):
            continue
        path = get_path(min_block, min_dir)
        shortest_line = get_shortest_line(path.copy())
        if shortest_line < MIN_STRAIGHT:
            continue
        s = 0
        for r in range(R):
            for c in range(C):
                if (r, c) in path:
                    s += grid[r][c] * path.count((r, c)) if (r, c) != (0, 0) else 0
                    # print(end='@')
                else:
                    pass
                    # print(end=str(grid[r][c]))
            # print()

        # print(f'{shortest_line=}')
        # print(s)
        # print()
        valid_paths.append((s, path))
print(min(valid_paths)[0])

# too low: 902
# too low: 915
# too low: 1196
