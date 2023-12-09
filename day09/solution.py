#!/usr/bin/env python3


def p1(lines):
    total = 0

    for l in lines:
        cur = [int(x) for x in l.split(" ")]
        diffs = get_diffs(cur)
        total += resolve_final(cur, diffs)

    print(f"Part 1: {total}")


def p2(lines):
    total = 0

    for l in lines:
        cur = [int(x) for x in l.split(" ")]
        diffs = get_diffs(reversed(cur))
        total += resolve_final(reversed(cur), diffs)

    print(f"Part 2: {total}")


def get_diffs(cur):
    c = list(cur)
    diffs = []

    while True:
        d = []

        for i in range(1, len(c)):
            d.append(c[i] - c[i - 1])

        diffs.append(d)
        c = d

        if len(set(d)) == 1:
            break

    return diffs


def resolve_final(cur, diffs):
    cur = list(cur)
    prev = diffs[-1][-1]

    for d in reversed(diffs[:-1]):
        prev = d[-1] + prev

    return cur[-1] + prev


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
