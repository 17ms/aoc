#!/usr/bin/env python3


import re


def p1(lines):
    total = 0
    pat = r"Card\s+\d+:\s+([\d ]+)\| ([\d ]+)"

    for l in lines:
        l_total = 0
        m = re.findall(pat, l)[0]

        own = [int(x) for x in m[0].split(" ") if x != ""]
        win = [int(x) for x in m[1].split(" ") if x != ""]

        for n in own:
            if n in win:
                if l_total == 0:
                    l_total = 1
                else:
                    l_total *= 2

        total += l_total

    print(f"Part 1: {total}")


def p2(lines):
    cards = 0
    extras = {n: 0 for n in range(len(lines) + 1)}

    pat = r"Card\s+([\d ]+):\s+([\d ]+)\| ([\d ]+)"

    for l in lines:
        l_total = 0
        m = re.findall(pat, l)[0]

        gid = int(m[0])
        own = [int(x) for x in m[1].split(" ") if x != ""]
        win = [int(x) for x in m[2].split(" ") if x != ""]

        extras[gid] += 1

        for n in own:
            if n in win:
                l_total += 1

        for n in range(gid + 1, gid + l_total + 1):
            extras[n] += extras[gid]

    for c in extras.values():
        cards += c

    print(f"Part 2: {cards}")


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
