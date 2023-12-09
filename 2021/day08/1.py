#!/usr/bin/env python

with open("input.txt") as f:
    lines = f.read().splitlines()

count = 0
for line in lines:
    l = line.split()
    outp = l[11:]
    for s in outp:
        lg = len(s)
        if lg in [2, 3, 4, 7]:
            count += 1

print(count)
    