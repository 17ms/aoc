#!/usr/bin/env python

with open("day21/input.txt") as f:
    p1, p2 = f.read().splitlines()
    p1 = p1.split()[-1]
    p2 = p2.split()[-1]
    players = [int(p1)-1, int(p2)-1]

board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [0, 0]
rolls = 0
dice = 1

# p1 always starts
active = 0

while max(scores) < 1000:
    steps = 0
    for i in range(3):
        if dice > 100: dice = 1
        steps += dice
        dice += 1
    rolls += 3
    total = players[active] + steps
    players[active] = total % 10
    scores[active] += board[players[active]]

    active = 1 if active == 0 else 0

loser = min(scores)
print(loser * rolls)
