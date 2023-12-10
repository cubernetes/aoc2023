#!/usr/bin/env python3

from collections import deque

data = open(0).read().strip()
lines = data.splitlines()
line_len = len(lines[0])
padded_lines = ['.' * line_len, *lines, '.' * line_len]
for i in range(len(padded_lines)):
    padded_lines[i] = list('.' + padded_lines[i] + '.')

def get_pipe_ends(pipe_type: str) -> tuple[int, int, int, int]:
    # (1, 1, 1, 1)
    #  N  S  W  E
    if pipe_type == 'S':
        return (1, 1, 1, 1)
    elif pipe_type == '|':
        return (1, 1, 0, 0)
    elif pipe_type == '-':
        return (0, 0, 1, 1)
    elif pipe_type == 'L':
        return (1, 0, 0, 1)
    elif pipe_type == 'J':
        return (1, 0, 1, 0)
    elif pipe_type == '7':
        return (0, 1, 1, 0)
    elif pipe_type == 'F':
        return (0, 1, 0, 1)
    elif pipe_type == '.':
        return (0, 0, 0, 0)
    else:
        assert False

def extend_pipes(padded_lines: list[str], pipes: deque) -> str:
    assert len(pipes) > 0
    if len(pipes) > 1:
        right_pipe_minus_1, right_pipe = pipes[-2], pipes[-1]
    else:
        right_pipe_minus_1, right_pipe = pipes[-1], pipes[-1]
    right_pipe_minus_1_type, row_right_pipe_minus_1, column_right_pipe_minus_1 = right_pipe_minus_1
    right_pipe_type, row_right_pipe, column_right_pipe = right_pipe
    if right_pipe_type == '.':
        return '.'
    open_ends = get_pipe_ends(right_pipe_type)
    if sum(open_ends) == 2 and right_pipe_type in 'LJ7F|-':
        if get_pipe_ends(p := padded_lines[row_right_pipe - 1][column_right_pipe])[1] and open_ends[0] and (row_right_pipe - 1, column_right_pipe) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            pipes.append((p,row_right_pipe - 1, column_right_pipe))
        elif get_pipe_ends(p := padded_lines[row_right_pipe + 1][column_right_pipe])[0] and open_ends[1] and (row_right_pipe + 1, column_right_pipe) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            pipes.append((p,row_right_pipe + 1, column_right_pipe))
        elif get_pipe_ends(p := padded_lines[row_right_pipe][column_right_pipe - 1])[3] and open_ends[2] and (row_right_pipe, column_right_pipe - 1) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            pipes.append((p,row_right_pipe, column_right_pipe - 1))
        elif get_pipe_ends(p := padded_lines[row_right_pipe][column_right_pipe + 1])[2] and open_ends[3] and (row_right_pipe, column_right_pipe + 1) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            pipes.append((p,row_right_pipe, column_right_pipe + 1))
        return pipes[-1][0]
    elif sum(open_ends) == 4 and right_pipe_type == 'S':
        tmp_pipes = deque()
        if get_pipe_ends(p := padded_lines[row_right_pipe - 1][column_right_pipe])[1] and open_ends[0] and (row_right_pipe - 1, column_right_pipe) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            tmp_pipes.append((p,row_right_pipe - 1, column_right_pipe))
        if get_pipe_ends(p := padded_lines[row_right_pipe + 1][column_right_pipe])[0] and open_ends[1] and (row_right_pipe + 1, column_right_pipe) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            tmp_pipes.append((p,row_right_pipe + 1, column_right_pipe))
        if get_pipe_ends(p := padded_lines[row_right_pipe][column_right_pipe - 1])[3] and open_ends[2] and (row_right_pipe, column_right_pipe - 1) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            tmp_pipes.append((p,row_right_pipe, column_right_pipe - 1))
        if get_pipe_ends(p := padded_lines[row_right_pipe][column_right_pipe + 1])[2] and open_ends[3] and (row_right_pipe, column_right_pipe + 1) != (row_right_pipe_minus_1, column_right_pipe_minus_1):
            tmp_pipes.append((p,row_right_pipe, column_right_pipe + 1))
        assert len(tmp_pipes) == 2
        pipes.appendleft(tmp_pipes[0])
        pipes.append(tmp_pipes[1])
        return pipes[-1][0]
    assert False

def find_S(padded_lines: list[str]) -> tuple[str, int, int]:
    for r, line in enumerate(padded_lines):
        for c, pipe_type in enumerate(line):
            if pipe_type == 'S':
                return 'S', r, c
    assert False

pipes = deque([find_S(padded_lines)])
while True:
    if extend_pipes(padded_lines, pipes) == 'S':
        break

print((len(pipes) - 1) // 2)
