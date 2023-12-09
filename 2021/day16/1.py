#!/usr/bin/env python

def parse(bits):
    global out_sum
    ver = bits[:3]
    out_sum += int(ver, 2)
    t_id = bits[3:6]
    bits = bits[6:]
    if t_id == "100":
        #print("literal value packet")
        while True:
            if bits[0] == "0":
                bits = bits[5:]
                break
            bits = bits[5:]
    else:
        #print("operator packet")
        lt_id = bits[0]
        bits = bits[1:]
        if lt_id == "0":
            ll = int(bits[:15], 2)
            bits = bits[15:]
            subs = bits[:ll]
            while subs:
                subs = parse(subs)
            bits = bits[ll:]
        elif lt_id == "1":
            amt = int(bits[:11], 2)
            bits = bits[11:]
            for _ in range(amt):
                bits = parse(bits)
    return bits

dd = {"0": "0000",
      "1": "0001",
      "2": "0010",
      "3": "0011",
      "4": "0100",
      "5": "0101",
      "6": "0110",
      "7": "0111",
      "8": "1000",
      "9": "1001",
      "A": "1010",
      "B": "1011",
      "C": "1100",
      "D": "1101",
      "E": "1110",
      "F": "1111"}

with open("input.txt") as f:
    transmission = list(f.read())
    binary = [dd[x] for x in transmission]
    binary = "".join(binary)

out_sum = 0
bits = parse(binary)
print(out_sum)
