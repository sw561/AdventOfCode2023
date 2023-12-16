#!/usr/bin/env python3

def read(fname):
    with open(fname, 'r') as f:
        return [line.strip() for line in f.readlines()]

step = {
    "E": (0, 1),
    "W": (0, -1),
    "N": (-1, 0),
    "S": (1, 0),
}

def propagate(d, i, j):
    dx, dy = step[d]
    return i+dx, j+dy

modifier = {"/": {"E": "N", "N": "E", "S": "W", "W": "S"},
    "\\": {"S": "E", "E": "S", "N": "W", "W": "N"},
    "|": {"E": "NS", "W": "NS", "N": "N", "S": "S"},
    "-": {"E": "E", "W": "W", "N": "EW", "S": "EW"}
    }

def new_directions(space, old_direction):
    if space == ".":
        yield old_direction
        return
    yield from modifier[space][old_direction]

def display(data, visited, to_consider):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if ("N", i, j) in to_consider:
                print("^", end='')
            elif ("S", i, j) in to_consider:
                print("v", end='')
            elif ("E", i, j) in to_consider:
                print(">", end='')
            elif ("W", i, j) in to_consider:
                print("<", end='')
            elif any((d, i, j) in visited for d in "NESW"):
                print("#", end='')
            else:
                print(data[i][j], end='')
        print()
    print("=======================================")


def solve_part1(data):
    # for line in data:
    #     print(line)
    # print("=======================================")

    # Do BFS but to visit a tile we need to have been there with the same
    # direction as before

    # Start off the edge of the board deliberately
    start = ('E', 0, -1)
    visited = set()

    to_consider = [start]

    while to_consider:
        new_to_consider = []

        for d, i, j in to_consider:

            # Simply move in the appropriate direction
            x, y = propagate(d, i, j)

            if not (0 <= x < len(data) and 0 <= y < len(data[0])):
                continue

            for new_d in new_directions(data[x][y], d):
                if (new_d, x, y) not in visited:
                    new_to_consider.append((new_d, x, y))
                    visited.add((new_d, x, y))


        to_consider = new_to_consider

        # display(data, visited, to_consider)

        # import pdb; pdb.set_trace()

    return len(set((x, y) for (_, x, y) in visited))

def solve_part2(data):
    return 0

def main():
    data = read("day16_lasers/input.txt")
    # data = read("day16_lasers/example")

    return solve_part1(data), solve_part2(data)


if __name__=="__main__":
    part1, part2 = main()
    print(part1)
    print(part2)
