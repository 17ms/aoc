#!/usr/bin/env python

with open("input.txt") as f:
    lines = f.read().splitlines()
    table = [list(l) for l in lines]

def low_point(x, y):
    value = int(table[y][x])
    t, b, l, r = None, None, None, None
    if y != 0:
        t = int(table[y-1][x])
    if y != len(table) - 1:
        b = int(table[y+1][x])
    if x != 0:
        l = int(table[y][x-1])
    if x != len(table[y]) - 1:
        r = int(table[y][x+1])

    for v in [t, b, l, r]:
        if v is not None:
            if v <= value: return 0
    return value + 1

risk_level = 0
for y, row in enumerate(table, 0):
    for x, char in enumerate(row, 0):
        low_t = low_point(x, y)
        if low_t: risk_level += low_t

print(risk_level)
