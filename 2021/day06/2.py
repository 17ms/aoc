#!/usr/bin/env python
from collections import defaultdict

with open("input.txt") as f:
    fish = list(map(int, f.read().split(",")))

chart = {}
for n in range(9):
    chart[n] = 0

for timer in fish:
    chart[timer] += 1
print(chart)

for day in range(256):
    cur_day = defaultdict(int)
    for n, value in chart.items():
        if n == 0:
            cur_day[8] += value
            cur_day[6] += value
        else:
            cur_day[n-1] += value
    # syncing progress to main chart
    chart = cur_day
    
print(sum(x for _, x in chart.items()))

# basically a copy of https://www.youtube.com/watch?v=fHlWM8CIrlI
