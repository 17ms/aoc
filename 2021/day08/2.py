#!/usr/bin/env python

with open("input.txt") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    l = line.split()
    l.remove("|")
    signals, output = l[:10], l[10:]
    defined = {0: "", 1: "", 2: "", 3: "", 4: "",
                5: "", 6: "", 7: "", 8: "", 9: ""}
    group1, group2 = [], []

    # defining unique and storing unknown in groups
    for s in signals:
        lg = len(s)
        if lg == 2: defined[1] = set(s)
        elif lg == 3: defined[7] = set(s)
        elif lg == 4: defined[4] = set(s)
        elif lg == 5: group1.append(set(s))
        elif lg == 6: group2.append(set(s))
        elif lg == 7: defined[8] = set(s)

    # masking the groups
    for s in group1:
        # 2, 3, 5
        if defined[7].issubset(set(s)):
            defined[3] = set(s)
        else:
            # 5 & 2 have no subsets from defined
            # instead from defined 3 long subsets of 4 match 5 but not 2
            match_len = len(set(s).intersection(defined[4]))
            if match_len == 3:
                defined[5] = set(s)
            else:
                defined[2] = set(s)

    for s in group2:
        # 0, 6, 9
        if defined[4].issubset(set(s)):
            defined[9] = set(s)
        else:
            if defined[7].issubset(set(s)):
                defined[0] = set(s)
            else:
                defined[6] = set(s)

    final = ""
    for s in output:
        for k, v in defined.items():
            js = sorted("".join([str(x) for x in v]))
            if js == sorted(s):
                final += str(k)
    total += int(final)

print(total)
