#!/usr/bin/env python
from numpy import prod

def parse(bits):
    t_id = int(bits[3:6], 2)
    bits = bits[6:]
    if t_id == 4:
        # literal value packets
        val = ""
        while True:
            val += bits[1:5]
            if bits[0] == "0":
                bits = bits[5:]
                break
            bits = bits[5:]
        return bits, int(val, 2)
    else:
        # operator packets
        packets = []
        lt_id = bits[0]
        bits = bits[1:]
        if lt_id == "0":
            ll = int(bits[:15], 2)
            bits = bits[15:]
            subs = bits[:ll]
            while subs:
                subs, val = parse(subs)
                packets.append(val)
            bits = bits[ll:]
        elif lt_id == "1":
            amt = int(bits[:11], 2)
            bits = bits[11:]
            for _ in range(amt):
                bits, val = parse(bits)
                packets.append(val)

        if t_id == 0:
            # sum packets 
            return bits, sum(packets)
        elif t_id == 1:
            # product packets 
            return bits, prod(packets)
        elif t_id == 2:
            # minimum packets
            return bits, min(packets)
        elif t_id == 3:
            # maximum packets
            return bits, max(packets)
        elif t_id == 5:
            # greater than packets
            return bits, int(packets[0] > packets[1])
        elif t_id == 6:
            # less than packets
            return bits, int(packets[0] < packets[1])
        elif t_id == 7:
            # equal to packets
            return bits, int(packets[0] == packets[1])

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

with open("day16/input.txt") as f:
    transmission = list(f.read())
    binary = [dd[x] for x in transmission]
    binary = "".join(binary)

bits, out = parse(binary)
print(out)
