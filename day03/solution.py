#!/usr/bin/env python3


def p1(lines):
    grid = [list(l) for l in lines]
    nums = get_total_nums(grid)
    total = 0
    visited = set()

    for key, (num, idxs) in nums.items():
        if key in visited:
            continue

        visited.update(idxs)

        for idx in idxs:
            if has_adj_symbol(grid, *idx):
                total += num
                break

    print(f"Part 1: {total}")


def p2(lines):
    grid = [list(l) for l in lines]
    nums = get_total_nums(grid)
    total = 0

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c != "*":
                continue

            adj = get_adj_nums(grid, nums, i, j)

            if len(adj) == 2:
                total += adj[0] * adj[1]

    print(f"Part 2: {total}")


def has_adj_symbol(grid, x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                cur = grid[nx][ny]

                if cur != "." and not cur.isnumeric():
                    return True

    return False


def get_adj_nums(grid, nums, x, y):
    keys = nums.keys()
    seen = set()
    res = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if (nx, ny) in seen or (nx, ny) not in keys:
                    continue

                seen.add((nx, ny))
                n, idxs = nums[(nx, ny)]
                res.append(n)

                for idx in idxs:
                    seen.add(idx)

    return res


def get_total_nums(grid):
    nums = {}  # idx -> (num, idxs)
    visited = set()

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if not c.isnumeric() or (i, j) in visited:
                continue

            visited.add((i, j))
            idxs = [(i, j)]
            num_str = c

            k = j + 1

            while k < len(grid[0]) and row[k].isnumeric():
                num_str += row[k]
                visited.add((i, k))
                idxs.append((i, k))
                k += 1

            for idx in idxs:
                nums[idx] = (int(num_str), idxs)

    return nums


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
