#!/usr/bin/env python
from math import ceil

with open("input.txt") as f:
    lines = f.readlines()

scores = {"(": 1, "[": 2, "{": 3, "<": 4}
corr1 = {")": "(", "]": "[", "}": "{", ">": "<"}
corr2 = {v: k for k, v in corr1.items()}

# remove corrupt lines
rm = []
for l in lines:
    stack = []
    for c in l.strip():
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        elif stack.pop() != corr1[c]:
            rm.append(l)
            break

lines = [x for x in lines if x not in rm]

score_ls = []
for l in lines:
    score = 0
    stack = []
    for c in l.strip():
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            stack.pop()
    if stack:
        for c in reversed(stack):
            score *= 5
            score += scores[c]
    score_ls.append(score)

score_ls.sort()
print(score_ls[ceil((len(score_ls) - 1) / 2)])
