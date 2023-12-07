#!/usr/bin/env python3

from collections import Counter

def parse(line):
    s = line.split()
    return s[0], int(s[1])

def read(fname):
    with open(fname, 'r') as f:
        return [
            parse(line) for line in f.read().strip().split('\n')
            ]

strength = {s: i for i, s in enumerate(reversed("AKQJT98765432X"))}
strength_part2 = {s: i for i, s in enumerate(reversed("AKQXT98765432J"))}

def key(hand, strength, part2=False):
    c = Counter(hand)
    if part2:
        # If only one type, we already have 5 of a kind
        if len(c) > 1 and c["J"]:

            # Most common non-joker
            most_common = max(
                (card for card in c.keys() if card!="J"),
                    key=lambda card: c[card]
                )

            c[most_common] += c["J"]
            del c["J"]

    return sorted(c.values(), reverse=True) + [strength[card] for card in hand]

def solve(data, part2=False):

    scores = {hand: key(hand, strength) for hand, _ in data}

    data.sort(key=lambda e: scores[e[0]])
    part1 = sum(rank*bid for rank, (_, bid) in enumerate(data, start=1))

    for hand, _ in data:
        if "J" in hand:
            # Update score for hands with jokers
            scores[hand] = key(hand, strength_part2, part2=True)

    data.sort(key=lambda e: scores[e[0]])
    part2 = sum(rank*bid for rank, (_, bid) in enumerate(data, start=1))

    return part1, part2

def main():
    data = read("day07_poker/input.txt")

    return solve(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
