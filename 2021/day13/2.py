#!/usr/bin/env python
from collections import deque

def fold_y(row):
    global table
    # flipping down
    sub_up, sub_down = table[:row], list(reversed(table[row+1:]))

    # adapting the size
    sz_up, sz_down = len(sub_up), len(sub_down)
    if sz_up > sz_down:
        # add dif * list of "."s
        dif = sz_up - sz_down
        for _ in range(dif):
            sub_down.insert(0, ["." for i in range(len(sub_down[0]))])
    elif sz_up < sz_down:
        # cut excessive from down
        dif = sz_down - sz_up
        sub_down = sub_down[len(sub_down)-dif:]
    
    # merging
    for y, v in enumerate(sub_down):
        for x, vv in enumerate(v):
            if sub_up[y][x] != "#" and vv != ".":
                sub_up[y][x] = vv
    table = sub_up

def fold_x(col):
    global table
    sub_left, sub_right = [], []
    for row in table:
        l, r = row[:col], row[col+1:]
        sub_left.append(l)
        sub_right.append(r)
    # flipping right
    for i in range(len(sub_right)):
        sub_right[i] = list(reversed(sub_right[i]))

    # adapting the size
    sz_left, sz_right = len(sub_left[0]), len(sub_right[0])
    if sz_left > sz_right:
        # insert the beginning of right with "."s
        dif = sz_left - sz_right
        for i in range(len(sub_right)):
            d = deque(sub_right[i])
            d.extendleft(["." for _ in range(dif)])
            sub_right[i] = list(d)
    elif sz_left < sz_right:
        # cut excessive from right
        dif = sz_right - sz_left
        for i in range(len(sub_right)):
            sub_right[i] = sub_right[i][:len(sub_right[i])-dif]
    
    # merging
    for y, v in enumerate(sub_right):
        for x, vv in enumerate(v):
            if sub_left[y][x] != "#" and vv != ".":
                sub_left[y][x] = vv
    table = sub_left
    
def better_print():
    global table
    for r in table:
        for i in r:
            if i == ".":
                print(" ", end="")
            else:
                print(i, end="")
        print("")

with open("input.txt") as f:
    p1, p2 = f.read().split("\n\n")
    # dots
    big_x = 0
    big_y = 0
    dots = []
    for d in p1.splitlines():
        x, y = d.split(",")
        if big_x < int(x): big_x = int(x)
        if big_y < int(y): big_y = int(y)
        dots.append((int(x), int(y)))
    #instructions
    instrus = []
    for i in p2.splitlines():
        tmp = i.split()[2].split("=")
        instrus.append((tmp[0], int(tmp[1])))

# creating 2d-table based on max coords
table = [["." for m in range(big_x+1)] for n in range(big_y+1)]
for d in dots: table[d[1]][d[0]] = "#"

for instr in instrus:
    det = instr[0]
    if det == "y":
        fold_y(instr[1])
    elif det == "x":
        fold_x(instr[1])

better_print()
