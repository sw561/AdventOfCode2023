#!/usr/bin/env python3

from functools import reduce
from string import digits
import operator
from collections import defaultdict

digits = set(digits)

def read(fname):
    with open(fname, 'r') as f:
        return f.read().strip().split()

def valid(x, y, nrows, ncols):
    return x >= 0 and x < nrows and y >= 0 and y < ncols

def construct_part_number(data, i, j, nrows, ncols):

    # Find first digit
    while 0 <= j-1 and data[i][j-1] in digits:
        j -= 1

    x = i
    y = j

    s = 0
    # Check all the digits
    while j < ncols and data[i][j] in digits:
        s = 10*s + int(data[i][j])
        j += 1

    return x, y, s

def neighbours(i, j, nrows, ncols):
    yield from (
        (x, y) for x in range(i-1,i+2) for y in range(j-1,j+2)
            if valid(x, y, nrows, ncols)
        )

def solve_part1(data):

    symbols = set().union(*data)
    symbols -= digits
    symbols.discard('.')

    print("symbols:", symbols)

    parts = {}


    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c in symbols:
                for nx, ny in neighbours(i, j, len(data), len(line)):
                    if data[nx][ny] in digits:
                        x, y, p = construct_part_number(data, nx, ny, len(data), len(line))
                        parts[(x, y)] = p


    for k, p in parts.items():
        print("k, p:", k, p)

    return sum(parts.values())

def solve_part2(data):
    gears = []
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '*':
                parts = {}
                for nx, ny in neighbours(i, j, len(data), len(line)):
                    if data[nx][ny] in digits:
                        x, y, p = construct_part_number(data, nx, ny, len(data), len(line))
                        parts[(x, y)] = p

                if len(parts) == 2:
                    gears.append(reduce(operator.mul, parts.values()))


    return sum(gears)

def main():
    data = read("day03_gear_ratios/input.txt")
    # data = read("day03_gear_ratios/example")

    # for line in data:
    #     print(line)

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
