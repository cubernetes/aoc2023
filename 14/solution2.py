#!/usr/bin/env python3

from copy import deepcopy

grid = list(map(list, open(0).read().strip().splitlines()))

def print_grid(grid: list[list[str]], lines: bool=False) -> None:
    for r in range(len(grid)):
        if lines:
            print(end=f'{str(len(grid) - r):>3} ')
        for c in range(len(grid[r])):
            print(end=grid[r][c])
        print()
    print()

def roll_down(grid: list[list[str]]) -> None:
    for r in range(len(grid) - 1, -1, -1):
        for c in range(len(grid[r])):
            if grid[r][c] == 'O':
                for down in range(r + 1, len(grid)):
                    if grid[down][c] == '.':
                        grid[down-1][c] = '.'
                        grid[down][c] = 'O'
                    else:
                        break
def roll_up(grid: list[list[str]]) -> None:
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'O':
                for up in range(r - 1, -1, -1):
                    if grid[up][c] == '.':
                        grid[up+1][c] = '.'
                        grid[up][c] = 'O'
                    else:
                        break

def transpose(grid: list[list[str]]) -> list[list[str]]:
    grid = [list(x) for x in zip(*grid)]
    return grid

def cycle(grid: list[list[str]]) -> list[list[str]]:
    roll_up(grid) # north
    grid = transpose(grid)
    roll_up(grid) # west
    grid = transpose(grid)
    roll_down(grid) # south
    grid = transpose(grid)
    roll_down(grid) # east
    grid = transpose(grid)
    return grid

def same_grid(grid1: list[list[str]], grid2: list[list[str]]) -> bool:
    for r in range(len(grid1)):
        for c in range(len(grid1[r])):
            if grid1[r][c] != grid2[r][c]:
                return False
    return True

def grid_load(grid: list[list[str]]) -> int:
    load = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'O':
                load += len(grid) - r
    return load

def get_phase_and_period(g: list[list[str]]) -> tuple[int, int]:
    states = []
    i = 0
    grid = deepcopy(g)
    while True:
        states.append(deepcopy(grid))
        grid = cycle(grid)
        for j, state in enumerate(states):
            if same_grid(grid, state):
                return j, i - j + 1
        i += 1

def repeat_period(grid: list[list[str]], n: int) -> list[list[str]]:
    for _ in range(n):
        grid = cycle(grid)
    return grid

iterations = 1_000_000_000
phase, period = get_phase_and_period(grid)
grid = repeat_period(grid, phase)

iterations -= phase
iterations = divmod(iterations, period)[1]
grid = repeat_period(grid, iterations)
print_grid(grid, lines=True)

print(grid_load(grid))
