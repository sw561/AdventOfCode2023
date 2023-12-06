#!/usr/bin/env python3

from functools import reduce
import operator

def parse(line):
    rest = line.split(':')[1]
    return [int(x) for x in rest.split()]

def read(fname):
    with open(fname, 'r') as f:
        times, distances = [parse(line) for line in f.read().strip().split('\n')]
    return times, distances

def distance(hold_time, time):
    return hold_time * (time - hold_time)

def winning_ways(data):
    for t, d in zip(*data):
        yield sum(1 for h in range(t) if distance(h, t) > d)

def solve_part1(data):
    return reduce(operator.mul, winning_ways(data))

def solve_part2(data):
    return 0

def main():
    data = read("day06_racing/input.txt")
    # data = read("day06_racing/example")

    print(data)

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
