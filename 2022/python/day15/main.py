#!/usr/bin/env python3

import re


def part_a(obs: list) -> None:
    Y = 2_000_000

    intervals = []

    for o in obs:
        # sx, sy, bx, by
        diff = abs(o[0] - o[2]) + abs(o[1] - o[3]) - abs(o[1] - Y)
        if diff > 0:
            intervals.append((o[0] - diff, o[0] + diff))

    beacons = [o[2] for o in obs if o[3] == Y]
    union = []

    for start, end in sorted(intervals):
        if union and union[-1][1] >= start - 1:
            union[-1][1] = max(union[-1][1], end)
        else:
            union.append([start, end])

    total = 0

    for u in union:
        for x in range(u[0], u[1] + 1):
            if x not in beacons:
                total += 1

    print(f"A: {total}")


def part_b(obs: list) -> None:
    incl = []
    decl = []

    for o in obs:
        d = abs(o[0] - o[2]) + abs(o[1] - o[3])
        incl.extend([o[0] - o[1] - d, o[0] - o[1] + d])
        decl.extend([o[0] + o[1] - d, o[0] + o[1] + d])

    # ref: https://github.com/womogenes/AoC-2022-Solutions/blob/main/day_15/day_15_p2.py
    for i in range(2 * len(obs)):
        for j in range(i + 1, 2 * len(obs)):
            a, b = incl[i], incl[j]

            if abs(a - b) == 2:  # the gap of 1 inside defined area
                pos = min(a, b) + 1

            a, b = decl[i], decl[j]

            if abs(a - b) == 2:
                neg = min(a, b) + 1

    print(f"B: {(pos + neg) // 2 * 4_000_000 + (neg - pos) // 2}")


observations = []

for l in open("input.txt", encoding="utf-8"):
    observations.append([int(x) for x in re.findall(r"-?\d+", l)])

part_a(observations)
part_b(observations)
