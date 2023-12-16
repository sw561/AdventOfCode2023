#!/usr/bin/env python3

from itertools import combinations, groupby

def read(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            s, ns = line.split(' ')
            ns = [int(n) for n in ns.split(',')]
            data.append((s, ns))

    return data

def valid_arrangements(s, ns):

    tot = sum(ns)

    print("s, ns:", s, ns)

    qs = [i for i in range(len(s)) if s[i] == "?"]
    nb = sum(1 for i in s if i == "#")

    # Need to break
    to_break = tot - nb

    valid_arrangements = 0

    for c in combinations(qs, to_break):
        candidate = "".join("#" if i in c or s[i]=="#" else "." for i in range(len(s)))

        gs = [len(list(g)) for k, g in groupby(candidate) if k == "#"]
        # print("c, candidate, gs:", c, candidate, gs)

        if gs == ns:
            valid_arrangements += 1

    return valid_arrangements

def solve_part1(data):
    total = 0
    for s, ns in data:
        total += valid_arrangements(s, ns)
    return total

def solve_part2(data):
    total = 0
    for s, ns in data:
        new_s = "?".join(s for i in range(5))
        new_ns = [n for i in range(5) for n in ns]
        total += valid_arrangements(new_s, new_ns)
    return total

def main():
    data = read("day12_broken_springs/input.txt")
    # data = read("day12_broken_springs/example")

    return solve_part1(data), 0# solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
