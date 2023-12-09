#!/usr/bin/env python
from collections import defaultdict

connections = defaultdict(set)

# recursive depth first search
def total_paths(s, visited):
    global connections
    count = 0
    if s == "end": return 1
    for con in connections[s]:
        if con not in visited:
            # checking for upper/lower case
            case = {con} if con.islower() else set()
            count += total_paths(con, visited | case)

    return count

with open("input.txt") as f:
    lines = f.read().splitlines()

# storing connections
for l in lines:
    p1, p2 = l.split("-")
    connections[p1].add(p2)
    connections[p2].add(p1)

print(total_paths("start", {"start"}))
