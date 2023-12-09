#!/usr/bin/env python

items = []
biggest = 0
with open("input.txt") as f:
    lines = f.read().replace(" ", "").replace("->", ",").splitlines()
    for l in lines:
        x, y, xx, yy = map(int, l.split(","))
        if max(x, y, xx, yy) > biggest:
            biggest = max(x, y, xx, yy)
        items.append((x, y, xx, yy))

board = [[0 for x in range(0, biggest + 1)] for y in range(0, biggest + 1)]

overlaps = 0
for t in items:
    x, y, xx, yy = [x for x in t]
    if x == xx:
        s = min(y, yy)
        e = max(y, yy) + 1
        for i in range(s, e):
            if board[i][x] == 1:
                board[i][x] = 2
                overlaps += 1
            elif board[i][x] == 0:
                board[i][x] = 1
    elif y == yy:
        s = min(x, xx)
        e = max(x, xx) + 1
        for i in range(s, e):
            if board[y][i] == 1:
                board[y][i] = 2
                overlaps += 1
            elif board[y][i] == 0:
                board[y][i] = 1
    else:
        # only addition to part 1
        dif_x, dif_y = xx - x, yy - y
        lim = abs(dif_x) + 1
        for _ in range(0, lim):
            cur_x = x + dif_x
            cur_y = y + dif_y
            if board[cur_y][cur_x] == 1:
                board[cur_y][cur_x] = 2
                overlaps += 1
            elif board[cur_y][cur_x] == 0:
                board[cur_y][cur_x] = 1
            if dif_x < 0: dif_x += 1
            else: dif_x -= 1
            if dif_y < 0: dif_y += 1
            else: dif_y -= 1

print(overlaps)
