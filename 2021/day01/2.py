#!/usr/bin/env python3

list = []
while True:
    line = input()
    if line:
        list.append(int(line))
    else:
        break

sums = []
i = 0
m = len(list)
while True:
    if i + 3 == m:
        s = sum(list[i:])
        sums.append(s)
        break
    s = sum(list[i:i+3])
    sums.append(s)
    i += 1

prev = None
count = 0
for i in sums:
    if prev and prev < i:
        count += 1
    prev = i

print(count)

