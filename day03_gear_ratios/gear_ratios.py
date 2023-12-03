#!/usr/bin/env python3

from functools import reduce
from string import digits
import operator

digits = set(digits)

def read(fname):
    with open(fname, 'r') as f:
        return f.read().strip().split()

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

def construct_part_numbers(data, i, j):
    nrows = len(data)
    ncols = len(data[0])
    for x in range(i-1,i+2):
        if x >= 0 and x < nrows:
            for y in range(j-1,j+2):
                if y >= 0 and y < ncols:
                    if data[x][y] in digits:
                        yield construct_part_number(data, x, y, nrows, ncols)

def solve(data):

    symbols = set().union(*data) - digits
    symbols.discard('.')

    parts = {}
    total_gears = 0

    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c not in symbols:
                continue

            local_parts = {(x, y): p for x, y, p in construct_part_numbers(data, i, j)}

            if c == "*" and len(local_parts) == 2:
                total_gears += reduce(operator.mul, local_parts.values())

            parts.update(local_parts)


    return sum(parts.values()), total_gears

def main():
    data = read("day03_gear_ratios/input.txt")
    # data = read("day03_gear_ratios/example")

    return solve(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
