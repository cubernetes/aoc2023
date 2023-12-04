#!/usr/bin/env python3

total = 0 
red, green, blue = 12, 13, 14
for i, line in enumerate(open(0)):
    def game_possible(line: str) -> bool:
        line = line.split(':')[1]
        sets_of_cubes = line.split('; ')
        for set_ in sets_of_cubes:
            selections = set_.split(', ')
            for selection in selections:
                amount, color = selection.split()
                amount = int(amount)
                if color == 'red' and amount > red:
                        return False
                if color == 'green' and amount > green:
                        return False
                if color == 'blue' and amount > blue:
                        return False
        return True
    if game_possible(line):
        total += i + 1

print(total)
