#!/usr/bin/env python3

from itertools import combinations

def read(fname):
    with open(fname, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    return data

def smaller_than(data, x):
    # Given a sorted list data find number of elements in data smaller than x
    # by bisection

    # data[left] < x
    left = 0
    # data[right] >= x
    right = len(data)-1

    if data[left] >= x:
        return 0

    if data[right] < x:
        return len(data)

    while right - left >= 2:
        c = (left + right) // 2

        if data[c] >= x:
            right = c
        else:
            left = c

    return right

def get_distance(left, right, expanded, ns):
    if left > right:
        left, right = right, left

    too_small = smaller_than(expanded, left)
    small_enough = smaller_than(expanded, right)
    extra = small_enough - too_small
    return [right - left + n * extra for n in ns]

def solve_part1(data, ns=[1]):

    stars = [(i, j) for i in range(len(data)) for j in range(len(data[0]))
        if data[i][j] == "#"
        ]

    sx = set(star[0] for star in stars)
    expanding_rows = [i for i in range(len(data)) if i not in sx]
    sy = set(star[1] for star in stars)
    expanding_cols = [i for i in range(len(data[0])) if i not in sy]

    total_distance = [0 for _ in ns]

    for star1, star2 in combinations(stars, 2):

        y_distance = get_distance(star1[0], star2[0], expanding_rows, ns)
        x_distance = get_distance(star1[1], star2[1], expanding_cols, ns)

        for j in range(len(ns)):
            total_distance[j] += x_distance[j] + y_distance[j]

    return total_distance

def main():
    data = read("day11_expanding_universe/input.txt")
    # data = read("day11_expanding_universe/example")

    return tuple(solve_part1(data, [1, 1_000_000 - 1]))


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
