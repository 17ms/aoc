#!/usr/bin/env python
from sys import maxsize
from collections import defaultdict, Counter

def default_val():
    return 0

with open("input.txt") as f:
    template, rules = f.read().split("\n\n")
    instrus = defaultdict(str)
    for r in rules.splitlines():
        tmp = r.split(" -> ")
        instrus[tmp[0]] = tmp[1]

# store all pairs in counter instead of a long string
count_pairs = Counter()
for i in range(len(template)-1):
    count_pairs[template[i:i+2]] += 1

for _ in range(40):
    new_pairs = Counter()
    for k in count_pairs.keys():
        a = instrus[k]
        p1, p2 = k[0]+a, a+k[1]
        new_pairs[p1] += count_pairs[k]
        new_pairs[p2] += count_pairs[k]
    count_pairs = new_pairs

# count the chars
count_chars = Counter({template[-1]: 1})
for p in count_pairs:
    count_chars[p[0]] += count_pairs[p]

high = 0
low = maxsize
for c in count_chars:
    high = max(count_chars[c], high)
    low = min(count_chars[c], low)

print(int(high - low))
