#!/usr/bin/env python3

import re


WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def p1(lines):
    s = 0

    for l in lines:
        nums = []

        for c in l:
            if c.isnumeric():
                nums.append(c)

        s += int(f"{nums[0]}{nums[-1]}")

    print(f"Part 1: {s}")


def p2(lines):
    s = 0

    for l in lines:
        line_nums = {}

        for k, v in WORDS.items():
            i = (m.start() for m in re.finditer(k, l))

            for ii in i:
                line_nums[ii] = v

        for i, c in enumerate(l):
            if c.isnumeric():
                line_nums[i] = c

        first = min(line_nums.keys())
        last = max(line_nums.keys())
        s += int(f"{line_nums[first]}{line_nums[last]}")

    print(f"Part 2: {s}")


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
