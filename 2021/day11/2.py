#!/usr/bin/env python

with open("input.txt") as f:
    lines = f.read().splitlines()
    table = []
    for l in lines:
        chars = []
        for c in l:
            chars.append(int(c))
        table.append(chars)

neighbours = [(-1, -1), (0, -1), (1, -1), 
              (-1, 0), (1, 0), 
              (-1, 1), (0, 1), (1, 1)]

def check_updates():
    global table
    count_u = 0
    for y in range(len(table)):
        for x in range(len(table[0])):
            if table[y][x] > 9:
                count_u += 1
    return count_u

# basically the only addition from part 1
def check_simultaneous():
    global table
    prev = table[0][0]
    for y in range(len(table)):
        for x in range(len(table[0])):
            if table[y][x] != prev:
                return False
            prev = table[y][x]
    return True

step = 0
while not check_simultaneous():
    step += 1
    # "can't flash more than once during a step"
    flashed = []

    # update every num by one
    for y in range(len(table)):
        for x in range(len(table[0])):
            table[y][x] += 1

    # looping while there's nums to update
    while check_updates() > 0:
        for y in range(len(table)):
            for x in range(len(table[0])):
                if table[y][x] > 9:
                    flashed.append((x, y))
                    table[y][x] = 0
                    for n in neighbours:
                        i = (x+n[0], y+n[1])
                        if i in flashed:
                            continue
                        elif 0 <= i[0] <= len(table[0]) - 1 and 0 <= i[1] <= len(table) - 1:
                            table[i[1]][i[0]] += 1

print(step)
