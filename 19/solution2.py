#!/usr/bin/env python3

from collections import defaultdict

workflows_, parts = map(str.splitlines, open(0).read().strip().split('\n\n'))
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
assert 'in' in workflows

def reverse_dependency(workflow: str, graph: list[str]) -> list[str]:
    if workflow == 'in':
        return graph
    for workflow_, rules in workflows.items():
        tmp_graph = []
        for condition, next_rule in rules:
            if next_rule == workflow:
                tmp_graph.append(condition)
                return reverse_dependency(workflow_, graph + tmp_graph)
            tmp_graph.append(invert_condition(condition))
    assert False

def invert_condition(condition):
    if condition == 'True':
        return 'False'
    name, rel, n = condition[0], condition[1], condition[2:]
    n = int(n)
    if rel == '>':
        return f'{name}<{n+1}'
    elif rel == '<':
        return f'{name}>{n-1}'
    assert False

def to_constraints(graph: list[str]) -> dict:
    constraints = {
        'x': [0, 4001],
        'm': [0, 4001],
        'a': [0, 4001],
        's': [0, 4001]
    }
    for cond in graph:
        if cond in ['True', 'False']:
            continue
        name, rel, n = cond[0], cond[1], cond[2:]
        n = int(n)
        if rel == '>':
            constraints[name][0] = max(constraints[name][0], n)
        elif rel == '<':
            constraints[name][1] = min(constraints[name][1], n)
        else:
            assert False
    return constraints

constraints = []
for workflow, rules in workflows.items():
    graph = []
    for condition, next_rule in rules:
        if next_rule == 'accept':
            graph.append(condition)
            constraints.append(to_constraints(reverse_dependency(workflow, graph)))
            graph.pop()
        graph.append(invert_condition(condition))

t = 1
for c in constraints:
    print(c)
    s = 1
    for min_, max_ in c.values():
        s *= max_ - min_ - 1
    t += s
print(t - 1)
