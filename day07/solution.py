#!/usr/bin/env python3


from collections import Counter
from operator import itemgetter


RANKS_REGULAR = "AKQJT98765432"
RANKS_JOKER = "AKQT98765432J"


def p1(lines):
    total = 0
    hands = []

    for l in lines:
        s = l.split(" ")
        v = assign_values(s[0])
        hands.append((classify(v), v, int(s[1])))

    hands.sort(reverse=True)

    for i, h in enumerate(hands):
        x = len(hands) - i
        total += x * h[2]

    print(f"Part 1: {total}")


def p2(lines):
    total = 0
    hands = []

    for l in lines:
        s = l.split(" ")
        hands.append((classify(replace_jokers(s[0])), assign_values(s[0], jokers=True), int(s[1])))

    hands.sort(reverse=True)

    for i, h in enumerate(hands):
        x = len(hands) - i
        total += x * h[2]

    print(f"Part 2: {total}")


def assign_values(hand, jokers=False):
    ranks = RANKS_JOKER if jokers else RANKS_REGULAR
    return [int(c) if c.isnumeric() else 14 - ranks.index(c) for c in hand.replace("J", "0")]


def classify(hand):
    c = Counter(hand).values()

    if 5 in c:
        t = 6  # five of a kind
    elif 4 in c:
        t = 5  # four of a kind
    elif 3 in c and 2 in c:
        t = 4  # full house
    elif 3 in c:
        t = 3  # three of a kind
    elif 2 in c and list(c).count(2) == 2:
        t = 2  # two pair
    elif 2 in c:
        t = 1  # one pair
    else:
        t = 0  # high card

    return t


def replace_jokers(hand):
    if "J" not in hand:
        return hand

    if hand == "JJJJJ":
        return "AAAAA"

    stripped = Counter(hand.replace("J", ""))
    sr, sr_c = get_replacements(hand, stripped)

    if len(stripped) in (1, 4):
        res = hand.replace("J", sr[0][0])  # five of a kind
    elif sum(stripped.values()) == 4:
        if max(stripped.values()) == 3 or min(stripped.values()) == 1:
            res = hand.replace("J", sr_c[-1][0])  # three or four of a kind
        else:
            res = hand.replace("J", sr[-1][0])  # full house
    elif sum(stripped.values()) == 3:
        if max(stripped.values()) == 2:
            res = hand.replace("J", sr_c[-1][0])  # four of a kind
        else:
            res = hand.replace("J", sr[-1][0])  # three of a kind
    else:
        res = hand.replace("J", sr[-1][0])  # four of a kind

    return res


def get_replacements(hand, stripped):
    replacements = [(ch, RANKS_REGULAR.index(ch), stripped[ch]) for ch in hand if ch != "J"]
    sr = sorted(replacements, key=itemgetter(1))
    sr_c = sorted(sr, key=itemgetter(2))

    return sr, sr_c


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
