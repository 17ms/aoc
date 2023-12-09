#!/usr/bin/env python3

# oxygen generator
def ol(list, l):
    for i in range(0, l):
        if len(list) == 1:
            break
        t = []
        for e in list:
            t.append(e[i])
        d = {"1": t.count("1"), "0": t.count("0")}
        if d["1"] == d["0"]:
            bit = "1"
        else:
            bit = max(d, key=d.get)
        for r in list.copy():
            if r[i] != bit:
                list.remove(r)

    return int(list[0], 2)

# co2 scrubber
def sl(list, l):
    for i in range(0, l):
        if len(list) == 1:
            break
        t = []
        for e in list:
            t.append(e[i])
        d = {"1": t.count("1"), "0": t.count("0")}
        if d["1"] == d["0"]:
            bit = "0"
        else:
            bit = min(d, key=d.get)
        for r in list.copy():
            if r[i] != bit:
                list.remove(r)

    return int(list[0], 2)

with open("input.txt") as f:
    list = f.read().splitlines()

l = len(list[0])
oxy = ol(list.copy(), l)
scrub = sl(list.copy(), l)

print(oxy * scrub)
