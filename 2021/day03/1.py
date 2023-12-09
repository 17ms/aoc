#!/usr/bin/env python3
from collections import Counter

with open("input.txt") as f:
    list = f.read().splitlines()

gamma_str = ""
i = 0
l = len(list[0])

while i < l:
    temp = []
    for b in list:
        temp.append(b[i])
    data = Counter(temp)
    gamma_str += data.most_common(1)[0][0]
    i += 1

epsilon_str = "".join(["1" if i == "0" else "0" for i in gamma_str])
print(int(gamma_str, 2) * int(epsilon_str, 2))
