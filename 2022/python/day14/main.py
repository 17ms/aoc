#!/usr/bin/env python3

import sys


rocks = set()

for l in open("input.txt", encoding="utf-8"):
    cc = [tuple((map(int, c.split(",")))) for c in l.strip().split(" -> ")]

    for i, c in enumerate(cc[1:]):
        # assuming no diagonal movement
        x1, y1 = cc[i]
        x2, y2 = c

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                rocks.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                rocks.add((x, y1))

        rocks.add(cc[i - 1])
        rocks.add(c)

part_a = True
count = 0

void = max(r[1] for r in rocks)
floor = 2 + void

# takes astonishing 0.7s to run, complex numbers'd probably help out

while True:
    s = (500, 0)

    while True:
        if part_a and s[1] >= void:
            part_a = False
            print(f"A: {count}")

        if (s[0], s[1] + 1) not in rocks and s[1] + 1 != floor:
            s = (s[0], s[1] + 1)
        elif (s[0] - 1, s[1] + 1) not in rocks and s[1] + 1 != floor:
            s = (s[0] - 1, s[1] + 1)
        elif (s[0] + 1, s[1] + 1) not in rocks and s[1] + 1 != floor:
            s = (s[0] + 1, s[1] + 1)
        else:
            rocks.add(tuple(s))
            count += 1

            if s == (500, 0):
                print(f"B: {count}")
                sys.exit(0)

            break
