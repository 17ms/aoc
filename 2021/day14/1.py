#!/usr/bin/env python
from collections import defaultdict, Counter

with open("input.txt") as f:
    template, rules = f.read().split("\n\n")
    instrus = defaultdict(str)
    for r in rules.splitlines():
        tmp = r.split(" -> ")
        instrus[tmp[0]] = tmp[1]

for _ in range(10):
    new_template = ""
    i = 0
    while i < len(template)-1:
        p = "".join([template[i], template[i+1]])
        a = instrus[p]
        new_template += template[i] + a
        i += 1
    new_template += template[-1]
    template = new_template

counts = Counter()
for c in template:
    counts[c] += 1

cc = sorted(counts.values())
print(cc[-1] - cc[0])
