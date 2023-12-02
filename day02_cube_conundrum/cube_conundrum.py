#!/usr/bin/env python3

from functools import reduce
import operator

translator = {"red": 0, "green": 1, "blue": 2}

def read(fname):
    with open(fname, 'r') as f:
        games = {}
        for line in f.read().strip().split('\n'):
            start, rest = line.split(': ')

            number = int(start.split()[1])

            views = []
            for g in rest.split('; '):
                view = [0, 0, 0]

                for c in g.split(', '):
                    n, color = c.split(' ')
                    n = int(n)
                    view[translator[color]] = n

                views.append(view)

            games[number] = views

    return games

def possible(views, maximal=[12, 13, 14]):
    return all(
        all(vi <= mi for vi, mi in zip(view, maximal))
            for view in views
        )

def solve_part1(data):
    return sum(
        id for id, views in data.items()
            if possible(views)
        )

def minimal(views):
    return map(max, zip(*views))

def solve_part2(data):
    return sum(
        reduce(operator.mul, minimal(views))
            for id, views in data.items()
        )

def main():
    data = read("day02_cube_conundrum/input.txt")
    # data = read("day02_cube_conundrum/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
