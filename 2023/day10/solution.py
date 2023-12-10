#!/usr/bin/env python3


DIRECTIONS = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
    "S": [(0, -1), (0, 1), (-1, 0), (1, 0)],
}

OPPOSITES = {
    (0, -1): (0, 1),
    (0, 1): (0, -1),
    (-1, 0): (1, 0),
    (1, 0): (-1, 0),
}


def p1(lines):
    grid = [list(l) for l in lines]
    start = find_start(grid)
    visited = find_loop(start, grid)

    print(f"Part 1: {max(visited.values())}")


def p2(lines, print_grid=False):
    grid = [list(l) for l in lines]
    start = find_start(grid)
    visited = find_loop(start, grid)

    replace_start(start, visited, grid)

    for y, row in enumerate(grid):
        pipes = 0  # count '|'

        for x, _ in enumerate(row):
            pos = grid[y][x]

            if (x, y) in visited:
                dirs = DIRECTIONS[pos]
                if (0, -1) in dirs:
                    pipes += 1
            elif pipes % 2 == 0:
                grid[y][x] = "O"
            else:
                grid[y][x] = "I"

    grid_str = "\n".join(["".join(line) for line in grid])

    if print_grid:
        print(grid_str)

    print(f"Part 2: {grid_str.count('I')}")


def find_start(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                start = (x, y)
                break

    return start


def find_loop(start, grid):
    visited = {}
    queue = [(start[0], start[1], 0)]

    while len(queue) > 0:
        x, y, dist = queue.pop(0)

        if (x, y) in visited:
            continue

        visited[(x, y)] = dist

        for dx, dy in DIRECTIONS[grid[y][x]]:
            nx, ny = x + dx, y + dy
            opp = OPPOSITES[(dx, dy)]

            if not 0 <= nx < len(grid[0]) or not 0 <= ny < len(grid):
                continue

            val = grid[ny][nx]

            if val not in DIRECTIONS:  # skip "."
                continue

            tgts = DIRECTIONS[val]

            if opp in tgts:
                queue.append((nx, ny, dist + 1))

    return visited


def replace_start(cur, visited, grid):
    sx, sy = cur
    reachable = []

    for pos, opp in OPPOSITES.items():
        dx, dy = pos
        nx, ny = sx + dx, sy + dy

        if not 0 <= nx < len(grid[0]) or not 0 <= ny < len(grid):
            continue

        if (nx, ny) not in visited:
            continue

        val = grid[ny][nx]

        if val not in DIRECTIONS:
            continue

        tgts = DIRECTIONS[val]

        if opp in tgts:
            reachable.append((dx, dy))

    for t, dirs in DIRECTIONS.items():
        if len(reachable) == len(dirs):
            if all(opp in dirs for opp in reachable):
                pt = t
                break

    grid[sy][sx] = pt


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
