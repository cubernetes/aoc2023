#!/usr/bin/env python3

from collections import defaultdict

workflows_, parts = map(str.splitlines, open(0).read().strip().split('\n\n'))
# lines = data.splitlines()
# lines = [list(line) for line in lines]
# R = len(lines)
# C = len(lines[0])
workflows = defaultdict(list)
for line in workflows_:
    name, rules = line.split('{') # }
    rules = rules[:-1].split(',')
    for rule in rules:
        if '>' in rule or '<' in rule:
            condition, rule = rule.split(':')
            if rule == 'A':
                rule = 'accept'
            elif rule == 'R':
                rule = 'reject'
            workflows[name].append((condition, rule))
        elif rule == 'A':
            workflows[name].append(('True', 'accept'))
        elif rule == 'R':
            workflows[name].append(('True', 'reject'))
        elif rule.islower():
            workflows[name].append(('True', rule))

def is_accepted(part: dict, workflow: str) -> bool:
    global workflows

    if 'in' not in workflows:
        assert False
    x = part['x']
    m = part['m']
    a = part['a']
    s = part['s']
    next_rule = ''
    for condition, rule in workflows[workflow]:
        if eval(condition):
            next_rule = rule
            break
    assert next_rule

    if next_rule == 'accept':
        return True
    elif next_rule == 'reject':
        return False
    return is_accepted(part, next_rule)

t = 0
for line in parts:
    part = {(a := x.split('='))[0]:int(a[1]) for x in line[1:-1].split(',')}
    if is_accepted(part, 'in'):
        t += sum(val for val in part.values())

print(t)
