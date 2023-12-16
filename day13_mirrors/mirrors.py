#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        blocks = f.read().strip().split('\n\n')
        blocks = [block.split('\n') for block in blocks]

    return blocks

def find_reflection(block):
    # for line in block:
    #     print(line)


    rocks = set((i, j) for i in range(len(block)) for j in range(len(block[0]))
        if block[i][j] == "#")

    # print(sorted(rocks))


    nR = len(block)
    nC = len(block[0])

    # print("nR:", nR)
    # print("nC:", nC)

    # try a reflection around column between 1 and 2 i.e. 1->2 and 0->3 etc



    # if nC = 9

    for r in range(1, nC):
        c = 2*r - 1
        # c is 1, 3, ..., 2*nC-3
        ref = set((i, c-j) for (i, j) in rocks if 0 <= c-j < nC)
        # print(sorted(ref))
        if ref <= rocks:
            # print("V: c, r, len(ref), ref <= rocks:", c, r, len(ref), ref <= rocks)
            return "V", r

    for r in range(1, nR):
        c = 2*r - 1
        ref = set((c-i, j) for (i, j) in rocks if 0 <= c-i < nR)
        # print(sorted(ref))
        if ref <= rocks:
            # print("H: c, r, len(ref), ref <= rocks:", c, r, len(ref), ref <= rocks)
            return "H", r

    import pdb; pdb.set_trace()


def solve_part1(data):
    total = 0
    for block in data:
        s, n = find_reflection(block)
        if s == "H":
            total += 100 * n
        else:
            assert s == "V"
            total += n
        # print("---------")
    return total


def solve_part2(data):
    return 0

def main():
    data = read("day13_mirrors/input.txt")
    # data = read("day13_mirrors/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
