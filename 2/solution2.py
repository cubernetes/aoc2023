#!/usr/bin/env python3

total = 0 
red, green, blue = 12, 13, 14
for i, line in enumerate(open(0)):
    def cube_set_power(line: str) -> int:
        max_red = max_green = max_blue = -1
        line = line.split(':')[1]
        sets_of_cubes = line.split('; ')
        for set_ in sets_of_cubes:
            selections = set_.split(', ')
            for selection in selections:
                amount, color = selection.split()
                amount = int(amount)
                if color == 'red' and amount > max_red:
                        max_red = amount
                if color == 'green' and amount > max_green:
                        max_green = amount
                if color == 'blue' and amount > max_blue:
                        max_blue = amount
        return max_red * max_green * max_blue
    total += cube_set_power(line)

print(total)
