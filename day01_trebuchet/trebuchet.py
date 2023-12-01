#!/usr/bin/env python3

import string

def read(fname):
    with open(fname, 'r') as f:
        return f.read().split()

def first_last(it):
    try:
        first = next(it)
    except StopIteration:
        print(list(it))
        raise
    last = first
    for i in it:
        last = i
    return first, last

def part1(line):
    f, l = first_last(x for x in line if x in string.digits)
    return 10 * int(f) + int(l)

def solve_part1(data):
    return sum(part1(line) for line in data)

written_digits = {1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"}

def repair(s):

    i = 0
    while i < len(s):
        for d, name in written_digits.items():
            if s[i:].startswith(name):
                s = s[:i] + str(d) + s[i+len(name):]
        i += 1

    return s


def solve_part2(data):
    rep = map(repair, data)

    r = list(rep)
    for i in range(len(data)):
        print(f"{data[i]:40s}, {r[i]:30s}, {part1(r[i]):3d}")
        # print("part1(r[i]):", part1(r[i]))

        # import pdb; pdb.set_trace()

    return solve_part1(r)

def main():
    data = read("day01_trebuchet/input.txt")
    # data = read("day01_trebuchet/example")
    # data = read("day01_trebuchet/example2")

    # print(data)

    # return solve_part1(data), solve_part2(data)
    return None, solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
