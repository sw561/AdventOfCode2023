#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        return f.read().strip().split(',')

def my_hash(x):
    h = 0
    for c in x:
        h = (h + ord(c))*17 % 256
    return h

def solve_part1(data):
    return sum(map(my_hash, data))


def solve_part2(data):
    return 0

def main():
    data = read("day15_hashmap/input.txt")
    # data = read("day15_hashmap/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
