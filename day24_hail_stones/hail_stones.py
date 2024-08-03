#!/usr/bin/env python3

import numpy as np
from itertools import combinations

def read(fname):
    pvs = []
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            pvs.append([[int(x) for x in part.split(',')] for part in line.split('@')])

    return pvs

def solve_part1(data, xymin, xymax):
    for e in data:
        print("e:", e)

    # x + t0 * v = y + t1 * u
    #
    #
    #
    # ( v0  -u0 ) ( t0 )   ( -x0 + y0 )
    # (         ) (    ) = (          )
    # ( v1  -u1 ) ( t1 )   ( -x1 + y1 )
    #
    #

    count_inside = 0

    for ((x, v), (y, u)) in combinations(data, 2):
        print("----")

        print("x, v:", x, v)
        print("y, u:", y, u)

        if v[0] * u[1] == v[1] * u[0]:
            print("Parallel")
            continue

        t0, t1 = np.linalg.solve([[v[0], -u[0]], [v[1], -u[1]]], [-x[0] + y[0], -x[1] + y[1]])

        # print("t0, t1:", round(t0, 3), round(t1, 3))

        if t0 < 0 or t1 < 0:
            print("Past")
            continue

        # Intersection point is at

        int_x = x[0] + t0 * v[0]
        int_y = x[1] + t0 * v[1]

        # print("int_x, int_y:", round(int_x, 3), round(int_y, 3))

        if xymin <= int_x <= xymax and xymin <= int_y <= xymax:
            print("Inside")
            count_inside += 1
        else:
            print("Outside")

    return count_inside


def solve_part2(data):
    return 0

def main():
    data = read("day24_hail_stones/input.txt")
    xymin = 200000000000000
    xymax = 400000000000000

    # data = read("day24_hail_stones/example")
    # xymin = 7
    # xymax = 27

    return solve_part1(data, xymin, xymax), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
