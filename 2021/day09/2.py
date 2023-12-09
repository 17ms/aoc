#!/usr/bin/env python
import numpy

with open("input.txt") as f:
    lines = f.read().splitlines()
    table = [list(l) for l in lines]

lows = []
used = []

def low_point(x, y):
    value = int(table[y][x])
    t, b, l, r = None, None, None, None
    if y != 0: t = int(table[y-1][x])
    if y != len(table) - 1: b = int(table[y+1][x])
    if x != 0: l = int(table[y][x-1])
    if x != len(table[y]) - 1: r = int(table[y][x+1])

    for v in [t, b, l, r]:
        if v is not None:
            if v <= value: return False
    return True

def find_basins(x, y, value, ):
    if (x, y) in used:
        return 0
    else:
        b_size = 1
        used.append((x, y))

    t, b, l, r = None, None, None, None
    if y != 0:
        t = (x, y-1)
    if y != len(table) - 1:
        b = (x, y+1)
    if x != 0:
        l = (x-1, y)
    if x != len(table[y]) - 1:
        r = (x+1, y)

    for v in [t, b, l, r]:
        if v is not None:
            val = int(table[v[1]][v[0]])
            if val != 9:
                b_size += find_basins(v[0], v[1], val)

    return b_size

# finding lows 
for y, row in enumerate(table, 0):
    for x, char in enumerate(row, 0):
        if low_point(x, y):
            lows.append((x, y, int(char)))
            
# finding basins around lows
basins = []
for low in lows:
    value = low[2]
    x, y = low[0], low[1]
    basins.append(find_basins(x, y, value))

basins.sort()
three = basins[-3:]
print(numpy.prod(three))
