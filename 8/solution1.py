#!/usr/bin/env python3

data = open(0).read().strip()
instructions, nodes = data.split('\n\n')
instructions = [inst == 'R' for inst in instructions]
node_lines = nodes.splitlines()

nodes = {}
for line in node_lines:
    start_node, left_right_nodes = line.split('=')
    start_node = start_node.strip()
    left_node, right_node = left_right_nodes.split(',')
    left_node = left_node.strip().strip('(')
    right_node = right_node.strip().strip(')')
    nodes[start_node] = (left_node, right_node)

def repeat_forever(iterable):
    while True:
        for c in iterable:
            yield c

total = 0
cur = 'AAA'
for inst in repeat_forever(instructions):
    if (cur := nodes[cur][inst]) == 'ZZZ':
        break
    total += 1

print(total)
