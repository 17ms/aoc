#!/usr/bin/env python3

import re


def p1(lines):
    mappings = get_mappings(lines)
    seeds = [int(n) for n in re.findall(r"(\d+)", lines[0])]
    finals = apply_maps(seeds, mappings)

    print(f"Part 1: {min(finals)}")


def p2(lines):
    mappings = get_mappings(lines)
    seeds = [int(n) for n in re.findall(r"(\d+)", lines[0])]
    seeds = list(zip(seeds[::2], seeds[1::2]))
    locations = apply_maps_to_ranges(seeds, mappings)

    print(f"Part 2: {min(l[0] for l in locations)}")


def get_mappings(lines):
    mappings = []

    for name in [
        "seed-to-soil map:",
        "soil-to-fertilizer map:",
        "fertilizer-to-water map:",
        "water-to-light map:",
        "light-to-temperature map:",
        "temperature-to-humidity map:",
        "humidity-to-location map:",
    ]:
        mappings.append(parse_map(lines, name))

    return mappings


def parse_map(lines, name):
    start = lines.index(name) + 1
    section = []

    for l in lines[start:]:
        if len(l) == 0:
            break

        nums = [int(n) for n in re.findall(r"(\d+)", l)]
        section.append(tuple(nums))

    return section


def apply_maps(seeds, mappings):
    finals = []

    for section in mappings:
        finals = []

        for s in seeds:
            mapped = False

            for dst, src, length in section:
                if src <= s < src + length:
                    finals.append(dst + (s - src))
                    mapped = True
                    break

            if not mapped:
                finals.append(s)

        seeds = finals

    return finals


def apply_maps_to_ranges(seeds, mappings):
    locations = []

    for p in seeds:
        remaining = [p]
        res = []

        for m in mappings:
            while remaining:
                cur = remaining.pop()

                for dst, src, length in m:
                    if cur[1] < src or src + length <= cur[0]:  # no overlapping ranges
                        continue

                    if src <= cur[0] <= cur[1] < src + length:  # partial overlap (left side)
                        offset = cur[0] - src
                        res.append((dst + offset, dst + offset + cur[1] - cur[0]))
                        break

                    if cur[0] < src <= cur[1] < src + length:  # partial overlap (right side)
                        offset = cur[1] - src
                        res.append((dst, dst + offset))
                        remaining.append((cur[0], src - 1))
                        break

                    if src <= cur[0] < src + length >= cur[1]:  # completely contained
                        offset = cur[0] - src
                        res.append((dst + offset, dst + length - 1))
                        remaining.append((src + length, cur[1]))
                        break

                    if cur[0] < src >= src + length <= cur[1]:  # completely containing
                        res.append((dst, dst + length - 1))
                        remaining.append((cur[0], src - 1))
                        remaining.append((src + length, cur[1]))
                        break

                    # no matching range, remain unchanged
                    res.append(cur)

            # apply the results to the next mapping
            remaining = res
            res = []

        locations.extend(remaining)

    return locations


with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

p1(lines)
p2(lines)
