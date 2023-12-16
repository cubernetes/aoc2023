#!/usr/bin/env python3

from collections import deque

grid = [list(line.strip()) for line in open(0) if line.strip()]
R = len(grid)
C = len(grid[0])

def simulate(start_r, start_c, start_dir, grid) -> int:
    i = 0
    energized = [[grid[r][c] for c in range(C)] for r in range(R)]
    beams = deque([[start_r, start_c, start_dir]])
    appended = []
    seen = {tuple(beams[0])}
    while beams:
        r, c, dir = beams[0]

        # energized[r][c] = '@'
        # print('i', i, 'len(beams)', len(beams))
        # print('beams', beams)
        # print('seen', list(sorted(seen)))
        # for r_ in range(R):
        #     for c_ in range(C):
        #         if grid[r_][c_] in '/\\|-' and energized[r_][c_] != '@':
        #             print(end=grid[r_][c_])
        #         else:
        #             print(end=energized[r_][c_])
        #     print()
        # print()
        energized[r][c] = '#'

        if grid[r][c] == '.':
            pass
        elif grid[r][c] == '-':
            if dir == 'north':
                dir = 'west'
                new_beam = [r, c, 'east']
                if new_beam not in appended:
                    appended.append(new_beam)
                    beams.append(new_beam)
            elif dir == 'south':
                dir = 'east'
                new_beam = [r, c, 'west']
                if new_beam not in appended:
                    appended.append(new_beam)
                    beams.append(new_beam)
            elif dir == 'east' or dir == 'west':
                pass
            else:
                assert False
        elif grid[r][c] == '|':
            if dir == 'east':
                dir = 'south'
                new_beam = [r, c, 'north']
                if new_beam not in appended:
                    appended.append(new_beam)
                    beams.append(new_beam)
            elif dir == 'west':
                dir = 'north'
                new_beam = [r, c, 'south']
                if new_beam not in appended:
                    appended.append(new_beam)
                    beams.append(new_beam)
            elif dir == 'north' or dir == 'south':
                pass
            else:
                assert False
        elif grid[r][c] == '/':
            if dir == 'east':
                dir = 'north'
            elif dir == 'west':
                dir = 'south'
            elif dir == 'south':
                dir = 'west'
            elif dir == 'north':
                dir = 'east'
            else:
                assert False
        elif grid[r][c] == '\\':
            if dir == 'east':
                dir = 'south'
            elif dir == 'west':
                dir = 'north'
            elif dir == 'south':
                dir = 'east'
            elif dir == 'north':
                dir = 'west'
            else:
                assert False
        else:
            assert False

        # over 1h on an almost undebuggable bug :')
        hit_wall = False
        if dir == 'east':
            if c < C - 1:
                c += 1
            else:
                hit_wall = True
        elif dir == 'west':
            if c > 0:
                c -= 1
            else:
                hit_wall = True
        elif dir == 'north':
            if r > 0:
                r -= 1
            else:
                hit_wall = True
        elif dir == 'south':
            if r < R - 1:
                r += 1
            else:
                hit_wall = True
        else:
            assert False

        if not hit_wall and (r, c, dir) not in seen:
            seen.add((r, c, dir))
            beams[0] = [r, c, dir]
        else:
            beams.popleft()
            if beams:
                seen = {tuple(beams[0])}
            energized[r][c] = '#'
        i += 1

    t = 0
    for r in range(R):
        for c in range(C):
            if energized[r][c] == '#':
                t += 1
    return t

energy = simulate(0, 0, 'east', grid)
print(energy)
