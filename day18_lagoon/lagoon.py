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


def display(state, sideA, sideB):
    imin = min(p[0] for p in state) - 1
    imax = max(p[0] for p in state) + 1
    jmin = min(p[1] for p in state) - 1
    jmax = max(p[1] for p in state) + 1

    for i in range(imin, imax+1):
        for j in range(jmin, jmax+1):
            if (i, j) in state:
                print('#', end='')
            elif (i, j) in sideA:
                print('X', end='')
            elif (i, j) in sideB:
                print('Y', end='')
            else:
                print('.', end='')
        print()

dxdy = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

d_inverse = {"L": "R", "R": "L", "U": "D", "D": "U"}

def solve_part1(data):

    pos = (0, 0)
    state = set()
    state.add(pos)

    for d, i, _ in data:
        for n in range(i):
            pos = tuple(ai + bi for ai, bi in zip(pos, dxdy[d]))
            state.add(pos)
    assert pos == (0, 0)

    # Now do bfs to fill the interior
    sideA = set()
    dA = deque()
    sideB = set()
    dB = deque()
    # Take one step in direction of first and last instruction to get an interior position
    for z in [0, 1]:
        pos = (0, 0)
        for i in [0, -1]:
            d, _, _ = data[i]
            if z == 0 and i == -1:
                # Reverse direction of last step
                d = d_inverse[d]
            pos = tuple(ai + bi for ai, bi in zip(pos, dxdy[d]))
        if z == 0:
            sideA.add(pos)
            dA.append(pos)
        else:
            sideB.add(pos)
            dB.append(pos)

    while dA and dB:
    # for _ in range(100):
        for d, s in zip([dA, dB], [sideA, sideB]):

            pos = d.popleft()

            for dxy in dxdy.values():
                new_pos = tuple(ai + bi for ai, bi in zip(pos, dxy))

                if new_pos in s or new_pos in state:
                    continue

                s.add(new_pos)
                d.append(new_pos)

    return len(state) + (len(sideB) if dA else len(sideA))

def solve_part2(data):
    return 0

def main():
    data = read("day18_lagoon/input.txt")
    # data = read("day18_lagoon/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
