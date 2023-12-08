#!/usr/bin/env python3

from functools import reduce
from math import gcd

def read(fname):

    data = dict()

    with open(fname, 'r') as f:
        start, rest = f.read().strip().split('\n\n')
        instructions = start

        for line in rest.split('\n'):
            node, options = line.split(' = ')
            options = options[1:-1].split(', ')

            data[node] = options

    return instructions, data

def repeat(s):
    while True:
        yield from s

translate = {'L': 0, 'R': 1}

def solve_part1(data):
    instructions, data = data

    node = 'AAA'

    for i, s in enumerate(repeat(instructions), start=1):
        node = data[node][translate[s]]

        if node == "ZZZ":
            return i

def solve_part2(data):
    instructions, data = data

    nodes = [node for node in data.keys() if node.endswith('A')]

    good_path_lengths = [[] for node in nodes]

    for i, s in enumerate(repeat(instructions), start=1):
        nodes = [data[node][translate[s]] for node in nodes]

        for ni, node in enumerate(nodes):
            if node.endswith('Z'):
                good_path_lengths[ni].append(i)

                if all(good_path_lengths):
                    print("good_path_lengths:", good_path_lengths)

                    # For all the good path lengths, assert we have multiples of the
                    # first value

                    # for gp in good_path_lengths:
                    #     for x in gp[1:]:
                    #         assert x / gp[0] == x // gp[0]

                    # Find lowest common multiple
                    return reduce(lambda a, b: a*b//gcd(a,b),
                        (gp[0] for gp in good_path_lengths)
                        )


def main():
    data = read("day08_haunted_wasteland/input.txt")
    # data = read("day08_haunted_wasteland/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
