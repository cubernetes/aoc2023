#!/usr/bin/env python3

import math

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

def get_offset_and_period(nodes):
    zs = []
    for i, node in enumerate(nodes):
        if node.endswith('Z'):
            zs.append(i)
    assert len(zs) >= 3
    assert zs[1] - zs[0] == zs[2] - zs[1]
    return (zs[0], zs[2] - zs[1])

curs = []
for node in nodes:
    if node.endswith('A'):
        curs.append(node)

offsets_and_periods = []
for cur in curs:
    visited = []
    zs_found = 0
    for inst in repeat_forever(instructions):
        visited.append(cur)
        if (cur := nodes[cur][inst]) in visited:
            if zs_found == 3:
                break
        if cur.endswith('Z'):
            zs_found += 1
    offsets_and_periods.append(get_offset_and_period(visited))

# So apparently, for this problem, the offset of the first
# occurence of a node that ends with 'Z' is also the period
# of the next occurences...
print(math.lcm(*[offset_and_period[0] for offset_and_period in offsets_and_periods]))
