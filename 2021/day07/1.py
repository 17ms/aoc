#!/usr/bin/env python
from sys import maxsize

with open("input.txt") as f:
    nums = list(map(int, f.read().split(",")))

lowest = maxsize
for i in range(min(nums), max(nums) + 1):
    fuel = sum([abs(n - i) for n in nums])
    if fuel < lowest:
        lowest = fuel

print(lowest)
