#!/usr/bin/env python

def combinations(min_x, max_x, min_y, max_y):
    amount = 0
    # basically brute forcing
    for xvv in range(1, max_x + 1):
        for yvv in range(min_y, -min_y):
            x, y = 0, 0
            velx, vely = xvv, yvv
            while x <= max_x and y >= min_y:
                if x >= min_x and y <= max_y:
                    amount += 1
                    break
                
                x, y = (x + velx, y + vely)
                vely -= 1
                if velx > 0:
                    velx -= 1
                elif velx < 0:
                    velx += 1

    return amount

with open("input.txt") as f:
    line = f.read().split()
    x, y = line[2].replace("x=", "").replace(",", ""), line[3].replace("y=", "")
    x_a, y_a = [int(n) for n in x.split("..")], [int(n) for n in y.split("..")]
    min_x, max_x = min(x_a), max(x_a)
    min_y, max_y = min(y_a), max(y_a)

total = combinations(min_x, max_x, min_y, max_y)
print(total)
