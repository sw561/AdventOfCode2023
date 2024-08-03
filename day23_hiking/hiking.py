#!/usr/bin/env python3

from copy import copy
from collections import defaultdict
from string import ascii_letters

def read(fname):
    with open(fname, 'r') as f:
        return f.read().strip().split()

def neighbours_part1(data, i, j):
    if data[i][j] == ">":
        yield i, j+1

    elif data[i][j] == "<":
        yield i, j-1

    elif data[i][j] == "v":
        yield i+1, j

    elif data[i][j] == "^":
        yield i-1, j

    else:
        yield from neighbours_part2(data, i, j)

def neighbours_part2(data, i, j):
    for ii, jj in [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= ii < len(data) and 0 <= jj < len(data[0]):
            if data[ii][jj] != '#':
                yield ii, jj

def dfs_part1(data, starting_position):

    # stack contains (len of route to current pos, next_pos)

    stack = [(0, starting_position)]

    visited = dict()

    while stack:
        (L, next_pos) = stack.pop()

        # Remove previous exploration
        while len(visited) > L:
            # remove in LIFO order
            visited.popitem()

        visited[next_pos] = None

        for new_pos in neighbours_part1(data, *next_pos):
            if new_pos[0] == len(data) - 1:
                yield visited

            if new_pos in visited:
                continue

            stack.append((len(visited), new_pos))

def display_line(i, line, visited, labels):
    for j, char in enumerate(line):
        if (i, j) in visited:
            if labels is not None and (i, j) in labels:
                yield labels[(i, j)]
            else:
                yield 'O'
        else:
            yield char

def display(data, visited, labels=None):
    return "\n".join("".join(display_line(i, line, visited, labels)) for i, line in enumerate(data))


def solve_part1(data, part2=False):
    # Do depth first search
    starting_position = (0, data[0].find("."))

    longest_route = None
    longest_length = 0

    for r in dfs_part1(data, starting_position):
        if len(r) > longest_length:
            longest_route = copy(r)
            longest_length = len(r)

    return longest_route

def dfs_part2(edges, position, ending_position, visited, distance):

    for new_pos, steps in edges[position].items():
        if new_pos == ending_position:
            yield distance + steps
        if new_pos in visited:
            continue

        visited.add(new_pos)
        yield from dfs_part2(edges, new_pos, ending_position, visited, distance + steps)
        visited.remove(new_pos)

def solve_part2(data):
    # Start by finding junctions

    starting_position = (0, data[0].find("."))
    ending_position = (len(data) - 1, data[-1].find("."))

    junctions = set([starting_position, ending_position])

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != ".":
                continue

            s = sum(1 for _ in neighbours_part2(data, i, j))

            if s > 2:
                junctions.add((i, j))

    labels = {J: letter for J, letter in zip(junctions, ascii_letters)}

    print(display(data, junctions, labels))

    # Find reduced graph by doing path finding from each junction

    edges = defaultdict(dict)

    for junc in junctions:

        for next_pos in neighbours_part2(data, *junc):

            prev_pos = junc
            pos = next_pos
            n_steps = 1

            while pos not in junctions:
                count = 0
                next_pos = None
                for n in neighbours_part2(data, *pos):
                    if n == prev_pos:
                        continue

                    count += 1
                    next_pos = n

                assert count == 1

                prev_pos = pos
                pos = next_pos
                n_steps += 1

            edges[junc][pos] = n_steps


    translator = lambda p: labels.get(p, p)

    for k, v in edges.items():
        print(f"{translator(k)}:", end=" ")

        print("{" + ", ".join(f"{translator(kk)}: {vv}" for kk, vv in v.items()), end="}\n")

    visited = set()
    distance = 0

    # Now do dfs on the edges we have found
    return max(dfs_part2(edges, starting_position, ending_position, set(), 0))

def main():
    data = read("day23_hiking/input.txt")
    # data = read("day23_hiking/example")

    return len(solve_part1(data)), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
