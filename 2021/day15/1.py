#!/usr/bin/env python
from collections import defaultdict
from sys import maxsize

with open("input.txt") as f:
    lines = f.read().splitlines()
    table = [[int(n) for n in r] for r in lines]

# calculating safest path with dijkstra's 

th, tw = len(table), len(table[0])
start = (0, 0)
end = (th-1, tw-1)
heap_que = defaultdict(tuple)
heap_que[start] = 0
minimums = defaultdict(lambda: maxsize)
visited = set()

while heap_que:
    d = min(heap_que.values())
    cur = list(heap_que.keys())[list(heap_que.values()).index(d)]
    heap_que.pop(cur)
    #print(d, cur)

    if cur == end:
        print(d)
    elif cur in visited:
        continue
    else:
        visited.add(cur)

    # neighbours
    t, b = (cur[0]-1, cur[1]), (cur[0]+1, cur[1])
    l, r = (cur[0], cur[1]-1), (cur[0], cur[1]+1)
    for n in [t, b, l, r]:
        if n[0] < 0 or n[0] > th-1:
            continue
        elif n[1] < 0 or n[1] > tw-1:
            continue
        elif n in visited:
            continue

        n_val = table[n[0]][n[1]]
        n_dist = d + n_val
        if minimums[n] > n_dist:
            minimums[n] = n_dist
            heap_que[n] = n_dist
