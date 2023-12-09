#!/usr/bin/env python
import numpy as np
from functools import reduce

def enhance(img1, rounds):
    global filler
    for i in range(rounds):
        # padding to simulate infinite grid
        img1 = np.pad(img1, 2, constant_values=filler[(i+1)%2])
        img2 = np.ones(img1.shape, dtype=int) * filler[i%2]

        for n in range(1, img1.shape[0]-1):
            for m in range(1, img1.shape[1]-1):
                # formula (rr) pasted from reddit
                rr = reduce(lambda x, t: x*2+t, img1[(n-1):(n+2), (m-1):(m+2)].flat)
                img2[n, m] = algo[rr]
        
        img1 = img2
    return img1

with open("day20/input.txt") as f:
    algo, img = f.read().split("\n\n")
    algo.replace("\n", "")
    
img = np.array([[i == "#" for i in l] for l in img.splitlines()], dtype=int)
algo = np.array([i == "#" for i in algo], dtype=int)
# 1st and last check
filler = [algo[0], algo[-1] if algo[0] else algo[0]]

# for part 2 change 2 --> 50
ret = enhance(img, 2)
print(ret.sum())
