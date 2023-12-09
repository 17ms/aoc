#!/usr/bin/env python3

list = []
while True:
    line = input()
    if line:
        method, value = line.split(" ")
        list.append((method, int(value)))
    else:
        break

horizontal = 0
depth = 0
aim = 0

for i in list:
    if i[0] == "forward":
        horizontal += i[1]
        depth += aim * i[1]
    elif i[0] == "up":
        aim -= i[1]
    elif i[0] == "down":
        aim += i[1]

print(f"{horizontal * depth}")

