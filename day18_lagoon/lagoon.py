#!/usr/bin/env python3

from collections import deque

def read(fname, towards_interior):
    data = []
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            a, b, c = line.split(' ')
            b = int(b)
            c = c.strip('()#')
            data.append((a, b, c))
    return data, towards_interior


def display(state, interior):
    imin = min(p[0] for p in state) - 1
    imax = max(p[0] for p in state) + 1
    jmin = min(p[1] for p in state) - 1
    jmax = max(p[1] for p in state) + 1

    for i in range(imin, imax+1):
        for j in range(jmin, jmax+1):
            if (i, j) in state:
                print('#', end='')
            elif (i, j) in interior:
                print('X', end='')
            else:
                print('.', end='')
        print()

dxdy = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

d_inverse = {"L": "R", "R": "L", "U": "D", "D": "U"}

def solve_part1(data):
    data, towards_interior = data

    pos = (0, 0)
    state = set()
    state.add(pos)

    for d, i, _ in data:
        for n in range(i):
            pos = tuple(ai + bi for ai, bi in zip(pos, dxdy[d]))
            state.add(pos)
    assert pos == (0, 0)

    # Now do bfs to fill the interior
    s = set()
    # display(state, s)

    deq = deque()
    for d in towards_interior:
        pos = tuple(ai + bi for ai, bi in zip(pos, dxdy[d]))

    s.add(pos)
    deq.append(pos)

    # display(state, s)

    while deq:
        pos = deq.popleft()

        for dxy in dxdy.values():
            new_pos = tuple(ai + bi for ai, bi in zip(pos, dxy))

            if new_pos in s or new_pos in state:
                continue

            s.add(new_pos)
            deq.append(new_pos)

    # display(state, s)

    # print("len(state):", len(state))
    # print("len(s):", len(s))

    return len(state) + len(s)

def solve_part1_clever(data):
    data, towards_interior = data

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


        # print("pos:", pos)
        # print("enclosed_area:", enclosed_area)



    # print("perimeter:", perimeter)
    # print("enclosed_area:", enclosed_area)

    area = abs(enclosed_area) + perimeter // 2 + 1

    return area

direction = {'0': "R", '1': "D", '2': "L", '3': "U"}

def solve_part2(data):
    data, towards_interior = data

    new_data = []
    for _, _, x in data:
        distance = int(x[:5], 16)
        d = direction[x[5]]
        new_data.append((d, distance, x))

    # for d, i, _ in new_data:
    #     print("d, i:", d, i)

    return solve_part1_clever((new_data, towards_interior))

def main():
    data = read("day18_lagoon/input.txt", "DR")
    # data = read("day18_lagoon/example", "DR")
    # data = read("day18_lagoon/example2", "DR")

    # p1 = solve_part1(data)

    p1c = solve_part1_clever(data)

    p2 = solve_part2(data)

    print("p2:", p2)

    return p1c, p2


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
