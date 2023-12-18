#!/usr/bin/env python3

from collections import deque

def read(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            a, b, c = line.split(' ')
            b = int(b)
            c = c.strip('()#')
            data.append((a, b, c))
    return data

dxdy = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

def show_perimeter(data):
    pos = (0, 0)
    state = set()
    state.add(pos)

    for d, i, _ in data:
        for n in range(i):
            pos = tuple(ai + bi for ai, bi in zip(pos, dxdy[d]))
            state.add(pos)
    assert pos == (0, 0)

    imin = min(p[0] for p in state) - 1
    imax = max(p[0] for p in state) + 1
    jmin = min(p[1] for p in state) - 1
    jmax = max(p[1] for p in state) + 1

    for i in range(imin, imax+1):
        for j in range(jmin, jmax+1):
            if (i, j) in state:
                print('#', end='')
            else:
                print('.', end='')
        print()

def solve_part1(data):

    pos = (0, 0)
    perimeter = 0
    enclosed_area = 0 # by shoelace formula

    for d, n, _ in data:
        pos = tuple(ai + n * bi for ai, bi in zip(pos, dxdy[d]))

        perimeter += n
        if d == "L":
            enclosed_area -= pos[0] * n
        elif d == "R":
            enclosed_area += pos[0] * n

    area = abs(enclosed_area) + perimeter // 2 + 1

    return area

direction = {'0': "R", '1': "D", '2': "L", '3': "U"}

def solve_part2(data):

    new_data = []
    for _, _, x in data:
        distance = int(x[:5], 16)
        d = direction[x[5]]
        new_data.append((d, distance, x))

    return solve_part1(new_data)

def main():
    data = read("day18_lagoon/input.txt")
    # data = read("day18_lagoon/example")
    # data = read("day18_lagoon/example2")

    # show_perimeter(data)
    return solve_part1(data), solve_part2(data)

if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
