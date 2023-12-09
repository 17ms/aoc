#!/usr/bin/env python3


def get_adj(cube: tuple) -> set:
    x, y, z = cube
    return {
        (x, y, z + 1),
        (x, y, z - 1),
        (x, y + 1, z),
        (x, y - 1, z),
        (x + 1, y, z),
        (x - 1, y, z),
    }


def part_a(cubes: list) -> None:
    total = 0
    for c in cubes:
        for a in get_adj(c):
            if a not in cubes:
                total += 1

    print(f"A: {total}")


def part_b(cubes: list) -> None:
    # floodfill from outside
    min_x, max_x = min(x for x, y, z in cubes), max(x for x, y, z in cubes)
    min_y, max_y = min(y for x, y, z in cubes), max(y for x, y, z in cubes)
    min_z, max_z = min(z for x, y, z in cubes), max(z for x, y, z in cubes)

    air = {(min_x - 1, min_y - 1, min_z - 1)}
    todo = {(min_x - 1, min_y - 1, min_z - 1)}

    while todo:
        x, y, z = todo.pop()

        if (
            x not in range(min_x - 1, max_x + 2)
            or y not in range(min_y - 1, max_y + 2)
            or z not in range(min_z - 1, max_z + 2)
        ):
            continue

        new = get_adj((x, y, z))
        todo |= new - cubes - air
        air |= new

    print(f"B: {sum(len((get_adj((x, y, z)) & air) - cubes) for x, y, z in cubes)}")


cubes = {
    tuple(int(s) for s in l.split(",")) for l in open("input.txt", encoding="utf-8")
}

part_a(cubes)
part_b(cubes)
