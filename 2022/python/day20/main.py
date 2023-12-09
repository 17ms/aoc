#!/usr/bin/env python3

from copy import deepcopy


def solve(nums: list, indices: list, rounds: int = 1) -> int:
    for _ in range(rounds):
        for i, num in enumerate(nums):
            idx = indices.index(i)
            indices.pop(idx)
            indices.insert((idx + num) % len(indices), i)

        # print([nums[j] for j in indices])

    zero_idx = indices.index(nums.index(0))
    return sum(nums[indices[(zero_idx + i) % len(indices)]] for i in [1000, 2000, 3000])


values = [(i, int(l)) for i, l in enumerate(open("input.txt", encoding="utf-8"))]
nums, indices = [n for _, n in values], [i for i, _ in values]

print(
    f"A: {solve(nums, deepcopy(indices))}\nB: {solve([n * 811589153 for n in nums], deepcopy(indices), 10)}"
)
