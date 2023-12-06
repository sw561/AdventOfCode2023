#!/usr/bin/env python3

from functools import reduce
import operator
from math import sqrt, floor, ceil

def parse(line):
    rest = line.split(':')[1]
    return [int(x) for x in rest.split()], [int(rest.replace(' ',''))]

def read(fname):
    with open(fname, 'r') as f:
        times, distances = [parse(line) for line in f.read().strip().split('\n')]
    return zip(times, distances)

def distance(hold_time, time):
    return hold_time * (time - hold_time)

def brute_winning_ways(t, d):
    brute_min = min(h for h in range(t) if distance(h, t) > d)
    brute_max = max(h for h in range(t) if distance(h, t) > d)
    return brute_max - brute_min + 1

def winning_ways(t, d):
    # To get winning ways need to find the critical values...
    #
    #   x (t - x) = d
    #
    #   x^2 - tx + d = 0
    #
    #   x = t/2 +- sqrt(t**2/4 - d)

    r1 = t/2 - sqrt(t**2/4 - d)
    r2 = t/2 + sqrt(t**2/4 - d)

    my_min = floor(r1) + 1
    my_max = ceil(r2) - 1

    return my_max - my_min + 1

def solve(data):
    return reduce(operator.mul,
        (winning_ways(t, d) for t, d in zip(*data))
        )

def main():
    part1, part2 = read("day06_racing/input.txt")
    # part1, part2 = read("day06_racing/example")

    return solve(part1), solve(part2)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
