#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        blocks = f.read().strip().split('\n\n')
        blocks = [block.split('\n') for block in blocks]

    return blocks

def find_reflection(block):

    rocks = set((i, j) for i in range(len(block)) for j in range(len(block[0]))
        if block[i][j] == "#")

    nR = len(block)
    nC = len(block[0])

    part1 = None
    part2 = None

    for r in range(1, nC):
        c = 2*r - 1
        ref = set((i, c-j) for (i, j) in rocks if 0 <= c-j < nC)
        if ref <= rocks:
            part1 = r
        elif len(ref - rocks) == 1:
            part2 = r

        if not (part1 is None or part2 is None):
            return part1, part2

    for r in range(1, nR):
        c = 2*r - 1
        ref = set((c-i, j) for (i, j) in rocks if 0 <= c-i < nR)
        if ref <= rocks:
            part1 = 100*r
        elif len(ref - rocks) == 1:
            part2 = 100*r

        if not (part1 is None or part2 is None):
            return part1, part2

def solve(data):
    total_p1 = 0
    total_p2 = 0
    for block in data:
        p1, p2 = find_reflection(block)
        total_p1 += p1
        total_p2 += p2

    return total_p1, total_p2


def main():
    data = read("day13_mirrors/input.txt")
    # data = read("day13_mirrors/example")

    return solve(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
