#!/usr/bin/env python3

list = []
while True:
    line = input()
    if line:
        list.append(int(line))
    else:
        break

prev = None
count = 0
for i in list:
    if prev and prev < i:
        count += 1
    prev = i

print(count)

