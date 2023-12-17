#!/usr/bin/env python3

from heapq import *
from collections import defaultdict
import math

def read(fname):
    with open(fname, 'r') as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]

new_d = {"E": "NS", "N": "EW", "S": "WE", "W": "SN"}

def possible_directions(d, n):
    if n > 1:
        yield d

    yield from new_d[d]

dxdy = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}

def new_position(x, y, d):
    dx, dy = dxdy[d]
    return x+dx, y+dy

def valid(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])

def check(data, history):
    s = set(history)

    for i in range(len(data)):
        for j in range(len(data[0])):

            if (i, j) in s:
                print("#", end='')
            else:
                print(data[i][j], end='')
        print("   ", end='')
        for j in range(len(data[0])):

            print(data[i][j], end='')

        print()


def solve_part1(data):

    visited = dict()

    # heat_loss, i, j, direction, number of straight steps allowed
    start = (0, 0, 0, 'E', 3, ())
    visited[(0, 0, 'E', 3)] = 0

    h = []
    heappush(h, start)

    while h:

        hl, i, j, d, n, history = heappop(h)

        for newd in possible_directions(d, n):
            newi, newj = new_position(i, j, newd)

            if not valid(data, newi, newj):
                continue

            new_n = n-1 if newd==d else 3

            # if (newi, newj) == (0, 9):
            #     import pdb; pdb.set_trace()


            # if new_n < 0:
            #     import pdb; pdb.set_trace()

            new_hl = hl + data[newi][newj]

            if new_hl >= visited.get((newi, newj, newd, new_n), math.inf):
                continue

            new_history = history + ((newi, newj),)

            if newi == len(data)-1 and newj == len(data[0])-1:

                # check(data, new_history)

                # import pdb; pdb.set_trace()

                return new_hl

            visited[(newi, newj, newd, new_n)] = new_hl
            heappush(h, (new_hl, newi, newj, newd, new_n, new_history))


        # print(h)
        # import pdb; pdb.set_trace()







def solve_part2(data):
    return 0

def main():
    data = read("day17_lava_factory/input.txt")
    # data = read("day17_lava_factory/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
