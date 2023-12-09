#!/usr/bin/env python
from ast import literal_eval
from math import ceil

def add(num1, num2):
    nn = [num1, num2]
    return reduce(nn)

def reduce(pair):
    # check explode & split recursively
    ret, pair = explode(pair)
    if ret:
        return reduce(pair)
    else:
        ret, pair = split(pair)
        if ret:
            return reduce(pair)
        else:
            return pair

# pasted from internet, simplified and commented afterwards
def explode(pair):
    ss = str(pair)
    pp = []
    i = 0
    while i < len(ss):
        if ss[i] == "[":
            pp.append("[")
            i += 1
        elif ss[i] == ",":
            pp.append(",")
            i += 1
        elif ss[i] == "]":
            pp.append("]")
            i += 1
        elif ss[i] == " ":
            i += 1
        else:
            # appending a pair of nums to pp
            j = i
            while j < len(ss) and ss[j].isdigit():
                j += 1
            pp.append(int(ss[i:j]))
            i = j
    
    d = 0
    for i, c in enumerate(pp):
        if c == "[":
            d += 1
            if d == 5:
                l = pp[i+1]
                r = pp[i+3]
                ll, rr = None, None
                for j in range(len(pp)):
                    # checking for first left regular number
                    if isinstance(pp[j], int) and j < i:
                        ll = j
                    # checking for first right regular number
                    elif isinstance(pp[j], int) and j > i+3 and rr is None:
                        rr = j
                # adding rr & ll to r & l and replacing exploding pair with 0
                if rr is not None:
                    pp[rr] += r
                pp = pp[:i] + [0] + pp[i+5:]
                if ll is not None:
                    pp[ll] += l
                return True, literal_eval("".join([str(x) for x in pp]))
        elif c == "]":
            d -= 1
    return False, pair

def split(pair):
    # recursively check until int, then split
    if isinstance(pair, int):
        if pair >= 10:
            return True, [pair//2, ceil(pair/2)]
        else:
            return False, pair
    else:
        ret, p1 = split(pair[0])
        if ret:
            return True, [p1, pair[1]]
        else:
            ret, p2 = split(pair[1])
            return ret, [pair[0], p2]

def magnitude(pair):
    total = 0
    # left
    l = pair[0]
    if isinstance(l, list):
        total += 3 * magnitude(l)
    else:
        total += 3 * l
    # right
    r = pair[1]
    if isinstance(r, list):
        total += 2 * magnitude(r)
    else:
        total += 2 * r

    return total

with open("input.txt") as f:
    l = f.read().splitlines()
    l = [literal_eval(x) for x in l]

while len(l) > 1:
    l[0] = add(l[0], l[1])
    del l[1]

total = magnitude(l[0])
print(total)
