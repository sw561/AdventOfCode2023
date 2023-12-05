#!/usr/bin/env python3

def read(fname):
    cards = {}
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            start, rest = line.split(':')

            n = int(start.split()[1])

            winning, have = rest.split(' | ')
            winning = set(map(int, winning.split()))
            have = [int(x) for x in have.split()]

            cards[n] = (winning, have)

    return cards

def solve(data):
    part1 = 0
    n_copies = {k: 1 for k in data.keys()}

    for k in sorted(data.keys()):
        w, h = data[k]

        matching = sum(1 for hi in h if hi in w)

        part1 += 1 << (matching - 1) if matching > 0 else 0

        for s in range(k+1, k+1+matching):
            n_copies[s] += n_copies[k]

    return part1, sum(n_copies.values())

def main():
    data = read("day04_scratchcards/input.txt")
    # data = read("day04_scratchcards/example")

    return solve(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
