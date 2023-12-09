#!/usr/bin/env python
from collections import defaultdict

connections = defaultdict(set)

def total_paths_plus(s, visited):
    global connections
    count = 0
    if s == "end": return 1
    for con in connections[s]:
        if con not in visited:
            case = {con} if con.islower() else set()
            count += total_paths_plus(con, visited | case) 
        elif con != "start":
            # 2 visits allowed by doing a "2nd loop"
            count += total_paths(con, visited)

    return count

# paste from part 1
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

print(total_paths_plus("start", {"start"}))

# difference to part 1:
# limit for small cave (lowercase) is 2 instead of 1
