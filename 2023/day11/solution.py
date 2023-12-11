#!/usr/bin/env python3

from itertools import combinations
import numpy as np


def p1(lines):
    grid = np.array([list(l) for l in lines])

    _, cols = grid.shape
    rm = np.array(["#" not in row for row in grid])
    cm = np.array(["#" not in grid[:, col] for col in range(cols)])

    nodes = [(i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == "#"]
    pairs = combinations(nodes, 2)

    total = sum(manhattan(p, rm, cm, 1) for p in pairs)

    print(f"Part 1: {total}")


def p2(lines):
    grid = np.array([list(l) for l in lines])

    _, cols = grid.shape
    rm = np.array(["#" not in row for row in grid])
    cm = np.array(["#" not in grid[:, col] for col in range(cols)])

    nodes = [(i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == "#"]
    pairs = combinations(nodes, 2)

    total = sum(manhattan(p, rm, cm) for p in pairs)

    print(f"Part 2: {total}")


def manhattan(pair, row_mask, col_mask, exp_factor=999999):
    n1, n2 = pair
    x1, y1 = n1
    x2, y2 = n2

    base_dist = abs(x1 - x2) + abs(y1 - y2)
    add_row_dist = 0
    add_col_dist = 0

    if x1 != x2:
        add_row_dist = sum(row_mask[min(x1, x2) : max(x1, x2) + 1]) * exp_factor

    if y1 != y2:
        add_col_dist = sum(col_mask[min(y1, y2) : max(y1, y2) + 1]) * exp_factor

    return base_dist + add_row_dist + add_col_dist


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
