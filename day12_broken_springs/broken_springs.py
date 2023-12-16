#!/usr/bin/env python3

from itertools import combinations, groupby
from re import sub

def read(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            s, ns = line.split(' ')
            ns = tuple(int(n) for n in ns.split(','))
            data.append((s, ns))

    return data

def valid_arrangements_brute(s, ns):

    tot = sum(ns)

    # print("s, ns:", s, ns)

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
            # print("candidate:", candidate)
            valid_arrangements += 1

    return valid_arrangements

def valid_arrangements(s, ns, d, indent=0):
    # print("-"*indent, "".join(s), ns)

    if len(s) == 0:
        if len(ns) == 0:
            # print("Found valid arrangement")
            return 1
        else: # len(ns) > 0:
            return 0

    elif len(ns) == 0:
        if '#' not in s:
            # print("Found valid arrangement")
            return 1
        else:
            return 0

    ss = "".join(s)
    if (ss, ns) in d:
        return d[(ss, ns)]

    if s[0] == "?":
        ret = 0
        s[0] = "#"
        ret += valid_arrangements(s, ns, d, indent+1)
        ret += valid_arrangements(s[1:], ns, d, indent+1)
        # s[0] = "?"

    elif s[0] == "#":
        count_hashes = 1
        while count_hashes < len(s) and (
                s[count_hashes] == "#" or
                    (count_hashes < ns[0] and s[count_hashes] == "?")
                ):
            count_hashes += 1

        if count_hashes != ns[0]:
            ret = 0
        else:
            # Skip the following character independent of whether it's ? or .
            ret = valid_arrangements(s[count_hashes+1:], ns[1:], d, indent+1)

    elif s[0] == ".":
        ret = valid_arrangements(s[1:], ns, d, indent+1)

    d[(ss, ns)] = ret
    return ret

def solve_part1(data, part2=False, va=valid_arrangements):
    total = 0
    for s, ns in data:
        if part2:
            s = "?".join(s for i in range(5))
            ns = tuple(n for i in range(5) for n in ns)
        s = list(sub(r'\.+','.', s).strip('.'))
        v = valid_arrangements(s, ns, dict())
        total += v
    return total

def solve_part2(data):
    return solve_part1(data, part2=True)

def main():
    data = read("day12_broken_springs/input.txt")
    # data = read("day12_broken_springs/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
