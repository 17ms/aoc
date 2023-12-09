#!/usr/bin/env python3


def piece(i, y) -> tuple:
    # Each rock appears so that its left edge is two units away from the left wall and
    # its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).
    if i == 0:
        return ((2, y), (3, y), (4, y), (5, y))

    if i == 1:
        return ((3, y), (2, 1 + y), (3, 1 + y), (4, 1 + y), (3, 2 + y))

    if i == 2:
        return ((2, y), (3, y), (4, y), (4, 1 + y), (4, 2 + y))

    if i == 3:
        return ((2, 0 + y), (2, 1 + y), (2, 2 + y), (2, 3 + y))

    if i == 4:
        return ((2, y), (3, y), (2, 1 + y), (3, 1 + y))


def down(piece: list, static: tuple) -> (list, bool):
    new = set((x, y - 1) for x, y in piece)
    if any(n in static for n in new):
        return piece, False

    return new, True


def left(piece: list) -> list:
    new = set((x - 1, y) for x, y in piece)
    if any(x == 0 for (x, y) in piece) or any(n in static for n in new):
        return piece

    return new


def right(piece: list) -> list:
    new = set((x + 1, y) for x, y in piece)
    if any(x == 6 for (x, y) in piece) or any(n in static for n in new):
        return piece

    return new


def tops(static: set, top: int) -> tuple:
    tops = []

    for x in range(0, 7):
        y = top
        while (x, y) not in static and y > 0:
            y -= 1
        tops.append(top - y)

    return tuple(tops)


T = int(1e12)

jets = list(open("input.txt", encoding="utf-8").readline().strip())
static = set((x, 0) for x in range(0, 7))
cache = {}

top, top_adj, pc, pi, ji = 0, 0, 0, 0, 0

while pc < T:
    if pc == 2022:
        print(f"A: {top}")

    p = piece(pi, top + 4)

    while True:
        if jets[ji] == ">":
            p = right(p)
        else:
            p = left(p)

        p, movable = down(p, static)
        ji = (ji + 1) % len(jets)

        if not movable:
            break

    static |= p
    top = max(y for (x, y) in static)
    key = (tops(static, top), ji, pi)

    if key in cache:
        # not the most efficient caching, both parts run in ~2 seconds
        last_pc, last_top = cache[key]
        reps = (T - pc) // (pc - last_pc)
        top_adj += (top - last_top) * reps
        pc += (pc - last_pc) * reps

    cache[key] = (pc, top)
    pi = (pi + 1) % 5
    pc += 1

print(f"B: {top + top_adj}")
