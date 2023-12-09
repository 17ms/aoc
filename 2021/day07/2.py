#!/usr/bin/env python
from math import comb
from sys import maxsize

with open("input.txt") as f:
    nums = list(map(int, f.read().split(",")))

# fuel consumption follows triangular numbers
# 0, 1, 3, 6, 10, 15, 21, 28, 36, ...

lowest = maxsize
for i in range(min(nums), max(nums) + 1):
    fuel = sum([comb((abs(n - i)) + 1, 2) for n in nums])
    if fuel < lowest:
        lowest = fuel

print(lowest)
