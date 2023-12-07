#!/usr/bin/env python3

from collections import Counter
from itertools import chain

def parse(line):
    s = line.split()
    return s[0], int(s[1])

def read(fname):
    with open(fname, 'r') as f:
        return [
            parse(line) for line in f.read().strip().split('\n')
            ]

def pad_with_zeros(it, n):
    # Yield n items. Start by yielding from it, then yield zeros

    for i, x in enumerate(it):
        yield x

    yield from (0 for _ in range(i+1, n))

ranking = {s: i for i, s in enumerate(reversed("AKQJT98765432"))}

def key(hand):
    s = sorted(Counter(hand).values(), reverse=True)
    return list(chain(pad_with_zeros(s, 5), (ranking[card] for card in hand)))

def solve_part1(data):
    data.sort(key=lambda e: key(e[0]))

    return sum(rank*bid for rank, (h, bid) in enumerate(data, start=1))

def solve_part2(data):
    # print(data)
    return 0


def main():
    data = read("day07_poker/input.txt")
    # data = read("day07_poker/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
