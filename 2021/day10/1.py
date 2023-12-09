#!/usr/bin/env python

with open("input.txt") as f:
    lines = f.readlines()

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
correspond = {")": "(", "]": "[", "}": "{", ">": "<"}

score = 0
for l in lines:
    stack = []
    for c in l.strip():
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        elif stack.pop() != correspond[c]:
            score += scores[c]
            break

print(score)
