#!/usr/bin/env python3

import re


def p1(lines):
    maxs = {"red": 12, "green": 13, "blue": 14}
    total = 0

    game_id_pattern = r"Game (\d+):"
    color_pattern = r"(\d+) (\w+)"

    for l in lines:
        countable = True
        game_id = re.match(game_id_pattern, l).group(1)
        colors = re.findall(color_pattern, l)

        for c in colors:
            if int(c[0]) > maxs[c[1]]:
                countable = False
                break

        # print(f"ID: {game_id} --> {colors}, countable: {countable}")

        if countable:
            total += int(game_id)

    print(f"Part 1: {total}")


def p2(lines):
    total = 0

    color_pattern = r"(\d+) (\w+)"

    for l in lines:
        mins = {"red": 0, "green": 0, "blue": 0}
        colors = re.findall(color_pattern, l)

        for c in colors:
            mins[c[1]] = max(mins[c[1]], int(c[0]))

        power = mins["red"] * mins["green"] * mins["blue"]
        total += power

    print(f"Part 2: {total}")


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
