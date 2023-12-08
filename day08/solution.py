#!/usr/bin/env python3


import re
import math


def p1(lines):
    navs, nodes = parse_maps(lines)

    s = 0
    cn = "AAA"

    while cn != "ZZZ":
        l_or_r = navs[s % len(navs)] == "R"
        cn = nodes[cn][l_or_r]
        s += 1

    print(f"Part 1: {s}")


def p2(lines):
    navs, nodes = parse_maps(lines)

    cn = {k: v for k, v in nodes.items() if k[-1] == "A"}
    s = []

    for n in cn:
        sc = 0

        while n[-1] != "Z":
            l_or_r = navs[sc % len(navs)] == "R"
            n = nodes[n][l_or_r]
            sc += 1

        s.append(sc)

    print(f"Part 2: {math.lcm(*s)}")


def parse_maps(lines):
    navs = list(lines[0])
    nodes = {}

    for l in lines[2:]:
        m = re.findall(r"(\w{3})", l)
        nodes[m[0]] = (m[1], m[2])

    return navs, nodes


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
