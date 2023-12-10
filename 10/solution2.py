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
    print("Couldn't find start S")
    assert False

pipes = deque([find_S(padded_lines)])
while True:
    if extend_pipes(padded_lines, pipes) == 'S':
        break

insides = 0
for r, line in enumerate(padded_lines):
    for c, pipe_type in enumerate(line):
        contains = False
        for pipe in pipes:
            if pipe[1:] == (r, c):
                contains = True
        if not contains:
            padded_lines[r][c] = '.'
        else: # Unicode Box drawings
            if pipe_type == 'L':
                padded_lines[r][c] = '└'
            elif pipe_type == 'J':
                padded_lines[r][c] = '┘'
            elif pipe_type == '7':
                padded_lines[r][c] = '┐'
            elif pipe_type == 'F':
                padded_lines[r][c] = '┌'
            elif pipe_type == 'S':
                padded_lines[r][c] = '┼'

for r, line in enumerate(padded_lines):
    for c, pipe_type in enumerate(line):
        if pipe_type != '.':
            print(end=pipe_type)
        else: # uneven number of crossings means inside
            inside = False
            F_joint = []
            L_joint = []
            for i in range(c + 1, len(line)):
                if line[i] in '|':
                    inside = not inside
                elif line[i] == '┌':
                    if not F_joint:
                        F_joint.append('F')
                    else:
                        if F_joint[-1] == 'J':
                            F_joint.pop()
                            inside = not inside
                        else:
                            F_joint.append('F')
                elif line[i] == '┘':
                    if not F_joint:
                        F_joint.append('J')
                    else:
                        if F_joint[-1] == 'F':
                            F_joint.pop()
                            inside = not inside
                        else:
                            F_joint.append('J')
                elif line[i] == '└':
                    if not L_joint:
                        L_joint.append('L')
                    else:
                        if L_joint[-1] == '7':
                            L_joint.pop()
                            inside = not inside
                        else:
                            L_joint.append('L')
                elif line[i] == '┐':
                    if not L_joint:
                        L_joint.append('7')
                    else:
                        if L_joint[-1] == 'L':
                            L_joint.pop()
                            inside = not inside
                        else:
                            L_joint.append('7')
            if inside:
                insides += 1
                print(end='\033[32mI\033[m')
            else:
                print(end='\033[31mO\033[m')
    print(flush=True)

print(insides)
