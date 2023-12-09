#!/usr/bin/env python

with open("input.txt") as f:
    fish = list(map(int, f.read().split(",")))

for i in range(0, 80):
    for i, f in enumerate(fish):
        if f == 0:
            fish.append(9)
            fish[i] = 6
        else:
            fish[i] -= 1

print(len(fish))
