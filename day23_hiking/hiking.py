#!/usr/bin/env python3

from copy import copy

def read(fname):
    with open(fname, 'r') as f:
        return f.read().strip().split()

def neighbours(data, i, j):
    if data[i][j] == ">":
        yield i, j+1

    elif data[i][j] == "<":
        yield i, j-1

    elif data[i][j] == "v":
        yield i+1, j

    elif data[i][j] == "^":
        yield i-1, j

    else:
        for ii, jj in [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < len(data) and 0 <= jj < len(data[0]):
                if data[ii][jj] != '#':
                    yield ii, jj

def dfs(data, starting_position):

    # stack contains (len of route to current pos, next_pos)

    stack = [(0, starting_position)]

    visited = set()
    route = []

    while stack:
        (L, next_pos) = stack.pop()

        # Remove previous exploration
        while len(route) > L:
            visited.remove(route.pop())

        visited.add(next_pos)
        route.append(next_pos)

        for new_pos in neighbours(data, *next_pos):
            if new_pos[0] == len(data) - 1:
                yield visited

            if new_pos in visited:
                continue

            stack.append((len(route), new_pos))

def display_line(i, line, visited):
    for j, char in enumerate(line):
        yield 'O' if (i, j) in visited else char

def display(data, visited):
    return "\n".join("".join(display_line(i, line, visited)) for i, line in enumerate(data))


def solve_part1(data):
    # Do depth first search
    starting_position = (0, data[0].find("."))

    longest_route = None
    longest_length = 0

    for r in dfs(data, starting_position):
        if len(r) > longest_length:
            longest_route = copy(r)
            longest_length = len(r)

    return longest_route


def solve_part2(data):
    return 0

def main():
    data = read("day23_hiking/input.txt")
    # data = read("day23_hiking/example")

    return len(solve_part1(data)), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
