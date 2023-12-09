#!/usr/bin/env python3
import re

class Board:
    def __init__(self, grid):
        self.grid = grid
        self.skippable = False
        rows = []
        for i in range(5, 26, 5):
            rows.append(grid[i-5:i])
        cols = []
        for i in range(0, 5):
            cols.append(grid[i::5])
        
        self.total = [x for x in rows + cols]

    def win(self, called):
        for l in self.total:
            if (all(x in called for x in l)):
                self.skippable = True
                return True
        return False

    def skip(self):
        return self.skippable

    def score(self, called):
        unmarked = list(set(self.grid) - set(called))
        unmarked = [int(x) for x in unmarked]
        return unmarked

with open("input.txt") as f:
    order = f.readline().strip().split(",")
    grids = f.read().split("\n\n")

boards = []
for g in grids:
    g = re.sub(r"\n", " ", g)
    boards.append(Board(g.split()))

called = []
for num in order:
    called.append(num)
    for b in boards:
        if b.skip():
            continue
        elif b.win(called):
            unmarked = b.score(called)
            print(sum(unmarked) * int(num))
            quit()

