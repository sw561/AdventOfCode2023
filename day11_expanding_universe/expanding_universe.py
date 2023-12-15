#!/usr/bin/env python3

from itertools import combinations

def read(fname):
    with open(fname, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    return data

def get_distance(left, right, expanded):
    if left > right:
        left, right = right, left
    extra = sum(1 for e in expanded if left < e < right)
    return right - left + extra

def solve_part1(data):

    stars = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == "#"]

    print(stars)
    expanding_rows = [i for i in range(len(data)) if not any(i == star[0] for star in stars)]
    expanding_cols = [i for i in range(len(data[0])) if not any(i == star[1] for star in stars)]

    print("expanding_rows:", expanding_rows)
    print("expanding_cols:", expanding_cols)

    total_distance = 0

    for star1, star2 in combinations(stars, 2):

        y_distance = get_distance(star1[0], star2[0], expanding_rows)
        x_distance = get_distance(star1[1], star2[1], expanding_cols)

        total_distance += x_distance + y_distance



    return total_distance

def solve_part2(data):
    return 0

def main():
    data = read("day11_expanding_universe/input.txt")
    # data = read("day11_expanding_universe/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
