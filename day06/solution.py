#!/usr/bin/env python3

import re


def p1(lines):
    times = re.findall(r"(\d+)", lines[0])
    distances = re.findall(r"(\d+)", lines[1])
    races = list(zip(times, distances))

    total = 1

    for r in races:
        w = 0

        for hold_time in range(1, int(r[0])):
            if new_distance(hold_time, int(r[0])) > int(r[1]):
                w += 1

        total *= w

    print(f"Part 1: {total}")


def p2(lines):
    time = int("".join(re.findall(r"(\d+)", lines[0])))
    distance = int("".join(re.findall(r"(\d+)", lines[1])))

    total = 0

    for hold_time in range(1, time):
        if new_distance(hold_time, time) > distance:
            total += 1

    print(f"Part 2: {total}")


def new_distance(hold_time, race_time):
    return hold_time * (race_time - hold_time)


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
